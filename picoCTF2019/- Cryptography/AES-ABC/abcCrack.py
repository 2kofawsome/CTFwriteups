#!/usr/bin/env python3

#from Crypto.Cipher import AES
import os
import math, codecs

def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = codecs.decode(s_n, "hex")    
    #decoded = codecs.decode(s_n, "hex").decode('utf-8')
    #decoded = bytes.fromhex(s_n).decode()
    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0: 
        decoded = b"\0" * (BLOCK_SIZE - pad) + decoded
    return decoded
    return decoded


with open('body.enc.ppm', 'rb') as f:
    ct = f.read() #in hex

BLOCK_SIZE = 16
UMAX = int(pow(256, BLOCK_SIZE))

blocks = []
for i in range(len(ct) // BLOCK_SIZE):
    blocks.append(ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE]) #still hex

newBlocks = []


for i in range(len(blocks) - 1):
    prev = int.from_bytes(blocks[-(i+2)], "big") #int
    curr = int.from_bytes(blocks[-(i+1)], "big")
    if i == 0:

    result = ((UMAX + (curr-prev)) % UMAX)
    newBlocks.insert(0,result)

blocks = []
for n in newBlocks:
    blocks.append(to_bytes(n))

blocks = b"".join(blocks)

with open('final.enc.ppm', 'wb') as fw:
    fw.write(b"""P6
1895 820
255
""")
    fw.write(blocks)

print("done")
