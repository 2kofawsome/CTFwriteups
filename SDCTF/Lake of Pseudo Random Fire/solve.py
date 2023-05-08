
from os import urandom
import random
import binascii

from Crypto.Cipher import AES

key = urandom(16)
def fromHex(hex):
    msg = hex
    msg_comp = bytes(x ^ 0xff for x in msg) # bitwise complement of msg
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(msg) + cipher.decrypt(msg_comp) # concatenation of cipher.encrypt(msg) and cipher.decrypt(msg_comp)
    print(ciphertext)
    print(binascii.hexlify(ciphertext))

    msg = cipher.decrypt(msg_comp)
    msg_comp = bytes(x ^ 0xff for x in msg) # bitwise complement of msg
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(msg) + cipher.decrypt(msg_comp) # concatenation of cipher.encrypt(msg) and cipher.decrypt(msg_comp)
    print(ciphertext)
    print(binascii.hexlify(ciphertext))

fromHex(binascii.unhexlify("aa"*16))
print("aa"*16)

print((b"8f93aa976985a610b58a943fde79fc33debdcfa0f4ecf01bbea684d54916b075"[32:]).decode("utf-8"))
print("ab5843a7919d31b8fae9a1ad32073d6aaa7fd0fb6db92220a65e76b7e717b017"[32:])


from socket import socket
from telnetlib import Telnet

sock = socket()
sock.connect(('prf.sdc.tf', 1337))
res = sock.recv(1024)
for n in range(50):
    res = sock.recv(1024)
    print(res)
    sock.send(b'3\n')
    sock.recv(1024)
    sock.send(b'aa'*16 + b'\n')
    res = sock.recv(1024)[53:85]
    sock.send(b'3\n')
    sock.recv(1024)
    sock.send(res + b'\n')
    res = sock.recv(1024)[21:53]
    if res == b'55555555555555555555555555555555':
        sock.send(b'2\n')
    else:
        sock.send(b'1\n')
print(sock.recv(1024))
print(sock.recv(1024))
print(sock.recv(1024))

sock.close()
# sdctf{n07_V3rY_pS3uD0R4nD0m_a6d137}