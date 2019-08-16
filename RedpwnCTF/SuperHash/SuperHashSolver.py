
import hashlib, time, string

alphabet = list(string.printable)


start = time.time()
for a in alphabet:
    hashed = a
    for n in range(10):
        hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest().upper()
    if hashed == "CD04302CBBD2E0EB259F53FAC7C57EE2":
        print(a)
print(time.time()-start)


start = time.time()
for a in alphabet:
    for b in alphabet:
        hashed = a+b
        for n in range(10):
            hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest().upper()
        if hashed == "CD04302CBBD2E0EB259F53FAC7C57EE2":
            print(a+b)
print(time.time()-start)


start = time.time()
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            hashed = a+b+c
            for n in range(10):
                hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest().upper()
            if hashed == "CD04302CBBD2E0EB259F53FAC7C57EE2":
                print(a+b+c)
print(time.time()-start)


start = time.time()
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                hashed = a+b+c+d
                for n in range(10):
                    hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest().upper()
                if hashed == "CD04302CBBD2E0EB259F53FAC7C57EE2":
                    print(a+b+c+d)
print(time.time()-start)

