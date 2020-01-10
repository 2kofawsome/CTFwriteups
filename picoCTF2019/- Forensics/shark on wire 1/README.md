# AUR

shark on wire 1 - Points: 150 - (Solves: 162)Forensics - Unsolved
Solve
Hints
We found this packet capture. Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_606ee6b0b78f6987c7b12f43253b2d9b.
Try using a tool like Wireshark
What are streams?

***

playeda round enough I found it in the UDP stream of this one

0000   ff ff ff ff ff ff 00 0c 29 b9 02 a9 08 00 45 00   ÿÿÿÿÿÿ..)¹.©..E.
0010   00 1d 00 01 00 00 40 11 66 c2 0a 00 00 02 0a 00   ......@.fÂ......
0020   00 0c 13 88 22 b8 00 09 82 8e 33 00 00 00 00 00   ...."¸....3.....
0030   00 00 00 00 00 00 00 00 00 00 00 00               ............


picoCTF{StaT31355_636f6e6e}
