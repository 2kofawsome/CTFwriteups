import hashlib

hash = "7f4986da7d7b52fa81f98278e6ec9dcb"

import time, datetime

start = time.time()

date = datetime.date(2021, 9, 11)

while True:
    date = date - datetime.timedelta(days=1)
    newHash = hashlib.md5(("Aaron" + str(date.strftime('%Y%m%d'))).encode('utf-8')).hexdigest()
    if (newHash == hash):
        print(1)
        print(date.strftime('%Y%m%d'))
        break
    newHash = hashlib.md5(("aaron" + str(date.strftime('%Y%m%d'))).encode('utf-8')).hexdigest()
    if (newHash == hash):
        print(2)
        print(date.strftime('%Y%m%d'))
        break
    newHash = hashlib.md5((str(date.strftime('%Y%m%d')) + "Aaron").encode('utf-8')).hexdigest()
    if (newHash == hash):
        print(3)
        print(date.strftime('%Y%m%d'))
        break
    newHash = hashlib.md5((str(date.strftime('%Y%m%d')) + "aaron").encode('utf-8')).hexdigest()
    if (newHash == hash):
        print(4)
        print(date.strftime('%Y%m%d'))
        break

print(time.time() -start)