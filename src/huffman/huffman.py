import heapq
from collections import Counter
import json
import os


def bitstring_to_bytes(s):
    padding = 8 - len(s) % 8
    if padding != 8:
        s = s + '0' * padding 
    return bytes(int(s[i:i+8], 2) for i in range(0, len(s), 8)), padding

def bytes_to_bitstring(byte_data, padding):
    bit_string = ''.join(format(byte, '08b') for byte in byte_data)
    if padding != 8:
        bit_string = bit_string[:-padding]
    return bit_string

class TreeNode:
    def __init__(self, value: bytes, freq: int = 0):
        self.right: None | TreeNode = None
        self.left: None | TreeNode = None
        self.value = value
        self.freq = freq
    
    def __lt__(self, other):
        return self.freq < other.freq

def encode(inp: bytes) -> tuple[str, dict[bytes, str]]:
    if not inp:
        return "", {}

    if len(set(inp)) == 1:
        return "0" * len(inp), {inp[0:1]: "0"}
    
    output_string = ""
    dictionary = {}

    frequencies = Counter(inp)
    
    nodes = [TreeNode(bytes([char]), freq) for char, freq in frequencies.items()]
    heapq.heapify(nodes)
    
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        
        parent = TreeNode(left.value + right.value, left.freq + right.freq)
        parent.left = left
        parent.right = right
        
        heapq.heappush(nodes, parent)
    
    root = nodes[0]
    
    def walk(node, acc):
        if node.left is None and node.right is None:
            dictionary[node.value] = acc
        else:
            if node.left is not None:
                walk(node.left, acc + "0")
            if node.right is not None:
                walk(node.right, acc + "1")
    
    walk(root, "")
    
    for byte in inp:
        byte_key = bytes([byte])
        output_string += dictionary[byte_key]

    return (output_string, dictionary)

def decode(encoded: str, table: dict[bytes, str]) -> bytes:
    res = []
    curr_tok = ""
    
    reverse_table = {code: byte for byte, code in table.items()}
    
    for bit in encoded:
        curr_tok += bit
        if curr_tok in reverse_table:
            res.append(reverse_table[curr_tok])
            curr_tok = ""
    
    return b''.join(res)

def encode_file(path: str, new_path: str = None):
    with open(path, "rb") as file:
        file_bytes = file.read()
        file_extension = os.path.splitext(path)[1] 
        
        encoded_bits, table = encode(file_bytes)
        encoded_bytes, padding = bitstring_to_bytes(encoded_bits)
        
        metadata = {
            'table': {key.hex(): value for key, value in table.items()},
            'padding': padding,
            'original_size': len(file_bytes),
            'extension': file_extension 
        }
        
        metadata_json = (json.dumps(metadata) + '\n').encode("utf-8")

        if new_path is None:
            new_path = os.path.basename(path).split('.')[0] + '_encoded'
        with open(new_path, "wb") as new_file:
            new_file.write(metadata_json)
            new_file.write(encoded_bytes)

def decode_file(path: str, new_path: str = None):
    with open(path, 'rb') as f:
        first_line = f.readline().strip()
        metadata = json.loads(first_line)
        
        table_serializable = metadata['table']
        table = {bytes.fromhex(key): value for key, value in table_serializable.items()}
        padding = metadata['padding']
        extension = metadata.get('extension', '') 
        
        encoded_bytes = f.read()
        bit_string = bytes_to_bitstring(encoded_bytes, padding)
        decoded_bytes = decode(bit_string, table)
        
        if new_path is None:
            new_path = "decoded_file" + extension
        
        with open(new_path, "wb") as output_file:
            output_file.write(decoded_bytes)

        return new_path

def encode_text(text: str) -> tuple[str, dict[bytes, str]]:
    output_string, dictionary = encode(text.encode("utf-8"))    
    return (output_string, dictionary)

def decode_text(encoded: bytes, table: dict[bytes, str]) -> bytes:
    return decode(encoded, table).decode("utf-8")

