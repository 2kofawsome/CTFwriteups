import string, sys, hashlib, binascii, string
from Crypto.Cipher import AES

alpha = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list("_")


while True:
    hey = str.encode(input())

    for n in alpha:
        for m in alpha:
            key = (n + m) *16
            cipher = AES.new(str.encode(key), AES.MODE_ECB)
            pt = cipher.decrypt(binascii.unhexlify(hey))
            try:
                pt.decode('ascii')
                print(pt)
                print(n)
                print(m)
            except:
                continue
