file = 1000

import tarfile, os


for n in range(10):
    tf = tarfile.open(str(file)+".tar")
    tf.extractall()
    os.remove("filler.txt")
    os.remove(str(file)+".tar")
    file -= 1
