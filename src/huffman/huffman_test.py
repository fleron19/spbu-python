from huffman import encode_text, decode_text, encode_file, decode_file
import filecmp
import os

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
    size = 1024
    with open("random", "wb") as fout:
        fout.write(os.urandom(size)) 

        encode_file("random")
        decode_file("random_encoded", "res")
        assert filecmp.cmp("random", "res")
