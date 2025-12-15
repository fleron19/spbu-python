from hamming import encode, decode


def test_encode():
    s = encode("Hi")
    assert s == '1001100011011000101'

def test_decode_right():
    s = encode("Hi")
    r = decode(s)
    assert r == -1

def test_decode_wrong():
    s = '1011100011011000101'
    r = decode(s)
    assert r == 2



