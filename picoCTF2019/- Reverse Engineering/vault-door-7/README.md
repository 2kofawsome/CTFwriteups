# AUR

vault-door-7 - Points: 400 - (Solves: 190)Reverse Engineering - Unsolved
Solve
Hints
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java
Use a decimal/hexademical converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
You will also need to consult an ASCII table such as this one: https://www.asciitable.com/

***

https://www.binaryconvert.com/result_unsigned_int.html?decimal=056053057051050050050049050

01000001 01011111 01100010 00110001
01110100 01011111 00110000 01100110
01011111 01100010 00110001 01110100
01011111 01110011 01101000 00110001
01100110 01010100 01101001 01001110
01100111 01011111 01100110 00110001
01100001 00110010 01100010 00110001
00110011 00111000 00110111 01100100

https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html

picoCTF{A_b1t_0f_b1t_sh1fTiNg_f1a2b1387d}
