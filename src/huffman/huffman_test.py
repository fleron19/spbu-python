from huffman import encode_text, decode_text, encode_file, decode_file
import filecmp

def test_text_code():
    original = "Hello, world!"
    text, table = encode_text(original)
    decoded = decode_text(text, table)
    assert original == decoded

def test_empty_code():
    original = ""
    text, table = encode_text(original)
    decoded = decode_text(text, table)
    assert original == decoded

def test_file_code():
    encode_file("huffman.py")
    decode_file("huffman_encoded", "res.py")
    assert filecmp.cmp("huffman.py", "res.py")
