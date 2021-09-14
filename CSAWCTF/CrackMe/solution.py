import hashlib

hash = "a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c"

words = open("10-million-password-list-top-1000000.txt",'r').read().splitlines()

import time

start = time.time()


for word in words:
    newHash = hashlib.sha256(("sha256" + word).encode('utf-8')).hexdigest()
    if (newHash == hash):
        print(word)

print(time.time() -start)