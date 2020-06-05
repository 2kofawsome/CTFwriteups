import string, sys, hashlib, binascii, string
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

alpha = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list("_")
final = "midnight{xwJjPw4Vp0Zl19xIdaNuz6zTeMQ1wlNP}"

hashpieces = open("hashpieces.txt").read().split("\n")

def checkHash(line, one, two):
    hey = str.encode(line)

    for n in alpha:
        for m in alpha:
            key = (n + m) *16
            cipher = AES.new(str.encode(key), AES.MODE_ECB)
            pt = cipher.decrypt(binascii.unhexlify(hey))
            try:
                pt.decode('ascii')
                if n != final[one]:
                    print(one, n)
                if m != final[two]:
                    print(two, m)
            except:
                continue




FIB = fibseq(MAXFIBSIZE)
i = 0
output = ''
s = 0
while i < len(data):
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

    checkHash(hashpieces[s], flag1, flag2)
    s += 1
