import string, sys, hashlib, binascii
from Crypto.Cipher import AES
key = b"a" *42
data = b"b" * 203
if not len(data) >= 191:
    raise AssertionError
FIBOFFSET = 4919
MAXFIBSIZE = len(key) + len(data) + FIBOFFSET

def fibseq(n):
    out = [
     0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)]]

    return out


FIB = fibseq(MAXFIBSIZE)
i = 0
output = ''
s = 0
while i < len(data):
    s += 1
    data1 = data[(FIB[i] % len(data))]
    key1 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    flag1 = ((i + FIB[(FIBOFFSET + i)]) % len(key))
    i += 1
    data2 = data[(FIB[i] % len(data))]
    key2 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    flag2 = ((i + FIB[(FIBOFFSET + i)]) % len(key))
    i += 1
    tohash = bytes([data1, data2])
    toencrypt = hashlib.md5(tohash).hexdigest()
    thiskey = bytes([key1, key2]) * 16
    cipher = AES.new(thiskey, AES.MODE_ECB)
    enc = cipher.encrypt(str.encode(toencrypt))
    output += binascii.hexlify(enc).decode('ascii')
    print()
    print(s)
    print(flag1)
    print(flag2)

print(output)
