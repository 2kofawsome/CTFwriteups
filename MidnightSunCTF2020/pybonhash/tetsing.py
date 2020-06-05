import string, sys, hashlib, binascii

key = b"midnight{" + b"a" *32 + b"}"
#42 characters

data = b"a" * 137

FIBOFFSET = 4919
MAXFIBSIZE = len(key) + len(data) + FIBOFFSET
#4919 + 42 + len(data) (136 or 137) doesnt matter
#5056 or 5055

def fibseq(n):
    out = [
     0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)]]

    return out

FIB = fibseq(MAXFIBSIZE) #fibincoi sequence to 1 less than MAXFIBSIZE

i = 0
output = ''
while i < len(data):
    data1 = data[(FIB[i] % len(data))]
    key1 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    i += 1
    data2 = data[(FIB[i] % len(data))]
    key2 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    i += 1


    
    tohash = bytes([data1, data2])
    toencrypt = hashlib.md5(tohash).hexdigest()
    thiskey = bytes([key1, key2]) * 16
    if b"a" not in thiskey:
        print(thiskey)
        print(toencrypt)
        print(i)
        print("")

print(output)
