from . import compression as c

enc = c.Encryption()
huf = c.Huffman()
ham = c.Hamming()


def ee(data):
    e1 = enc.Encrypt(data)
    e2 = huf.encode(e1)
    e3 = ham.encode(e2)
    e4 = ham.makeError(e3)
    e5 = ham.ErrorCorrection(e4)
    e6 = ham.decode(e5)
    e7 = huf.decode(e6)
    e8 = enc.Decrypt(e7)

    a = len(data)*8
    b = len(e2)

    return [e1, e2, e3, e4, e5, e6, e7, e8, (a, b)]
