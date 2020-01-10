# AUR

13 - Points: 100 - (Solves: 670)Cryptography - Unsolved
Solve
Hints
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
This can be solved online if you don't want to do it by hand!
Walkthrough: No-ops (NOPs) can be very useful here. Read more about them here: https://lthieu.wordpress.com/2012/11/10/exploit-stack-based-buffer-overflow-using-nop-sled-technique/

***

https://rot13.com/
picoCTF{not_too_bad_of_a_problem}











0000000000001185 <main>:
    1185:       55                      push   %rbp
    1186:       48 89 e5                mov    %rsp,%rbp
    1189:       48 83 ec 50             sub    $0x50,%rsp
    118d:       48 8d 35 74 0e 00 00    lea    0xe74(%rip),%rsi        # 2008 <_IO_stdin_used+0x8>
    1194:       48 8d 3d 6f 0e 00 00    lea    0xe6f(%rip),%rdi        # 200a <_IO_stdin_used+0xa>
    119b:       e8 d0 fe ff ff          callq  1070 <fopen@plt>
    11a0:       48 89 45 e8             mov    %rax,-0x18(%rbp)
    11a4:       48 8d 35 68 0e 00 00    lea    0xe68(%rip),%rsi        # 2013 <_IO_stdin_used+0x13>
    11ab:       48 8d 3d 63 0e 00 00    lea    0xe63(%rip),%rdi        # 2015 <_IO_stdin_used+0x15>
    11b2:       e8 b9 fe ff ff          callq  1070 <fopen@plt>
    11b7:       48 89 45 e0             mov    %rax,-0x20(%rbp)
    11bb:       48 83 7d e8 00          cmpq   $0x0,-0x18(%rbp)
    11c0:       75 0c                   jne    11ce <main+0x49>
    11c2:       48 8d 3d 57 0e 00 00    lea    0xe57(%rip),%rdi        # 2020 <_IO_stdin_used+0x20>
    11c9:       e8 62 fe ff ff          callq  1030 <puts@plt>
    11ce:       48 83 7d e0 00          cmpq   $0x0,-0x20(%rbp)
    11d3:       75 0c                   jne    11e1 <main+0x5c>
    11d5:       48 8d 3d 7e 0e 00 00    lea    0xe7e(%rip),%rdi        # 205a <_IO_stdin_used+0x5a>
    11dc:       e8 4f fe ff ff          callq  1030 <puts@plt>
    11e1:       48 8b 55 e8             mov    -0x18(%rbp),%rdx
    11e5:       48 8d 45 b0             lea    -0x50(%rbp),%rax
    11e9:       48 89 d1                mov    %rdx,%rcx
    11ec:       ba 01 00 00 00          mov    $0x1,%edx
    11f1:       be 18 00 00 00          mov    $0x18,%esi
    11f6:       48 89 c7                mov    %rax,%rdi
    11f9:       e8 42 fe ff ff          callq  1040 <fread@plt>
    11fe:       89 45 dc                mov    %eax,-0x24(%rbp)
    1201:       83 7d dc 00             cmpl   $0x0,-0x24(%rbp)
    1205:       7f 0a                   jg     1211 <main+0x8c>
    1207:       bf 00 00 00 00          mov    $0x0,%edi
    120c:       e8 6f fe ff ff          callq  1080 <exit@plt>
    1211:       c7 45 f8 00 00 00 00    movl   $0x0,-0x8(%rbp)
    1218:       eb 23                   jmp    123d <main+0xb8>
    121a:       8b 45 f8                mov    -0x8(%rbp),%eax
    121d:       48 98                   cltq   
    121f:       0f b6 44 05 b0          movzbl -0x50(%rbp,%rax,1),%eax
    1224:       88 45 ff                mov    %al,-0x1(%rbp)
    1227:       0f be 45 ff             movsbl -0x1(%rbp),%eax
    122b:       48 8b 55 e0             mov    -0x20(%rbp),%rdx
    122f:       48 89 d6                mov    %rdx,%rsi
    1232:       89 c7                   mov    %eax,%edi
    1234:       e8 27 fe ff ff          callq  1060 <fputc@plt>
    1239:       83 45 f8 01             addl   $0x1,-0x8(%rbp)
    123d:       83 7d f8 07             cmpl   $0x7,-0x8(%rbp)
    1241:       7e d7                   jle    121a <main+0x95>
    1243:       c7 45 f4 08 00 00 00    movl   $0x8,-0xc(%rbp)
    124a:       eb 43                   jmp    128f <main+0x10a>
    124c:       8b 45 f4                mov    -0xc(%rbp),%eax
    124f:       48 98                   cltq   
    1251:       0f b6 44 05 b0          movzbl -0x50(%rbp,%rax,1),%eax
    1256:       88 45 ff                mov    %al,-0x1(%rbp)
    1259:       8b 45 f4                mov    -0xc(%rbp),%eax
    125c:       83 e0 01                and    $0x1,%eax
    125f:       85 c0                   test   %eax,%eax
    1261:       75 0c                   jne    126f <main+0xea>
    1263:       0f b6 45 ff             movzbl -0x1(%rbp),%eax
    1267:       83 c0 05                add    $0x5,%eax
    126a:       88 45 ff                mov    %al,-0x1(%rbp)
    126d:       eb 0a                   jmp    1279 <main+0xf4>
    126f:       0f b6 45 ff             movzbl -0x1(%rbp),%eax
    1273:       83 e8 02                sub    $0x2,%eax
    1276:       88 45 ff                mov    %al,-0x1(%rbp)
    1279:       0f be 45 ff             movsbl -0x1(%rbp),%eax
    127d:       48 8b 55 e0             mov    -0x20(%rbp),%rdx
    1281:       48 89 d6                mov    %rdx,%rsi
    1284:       89 c7                   mov    %eax,%edi
    1286:       e8 d5 fd ff ff          callq  1060 <fputc@plt>
    128b:       83 45 f4 01             addl   $0x1,-0xc(%rbp)
    128f:       83 7d f4 16             cmpl   $0x16,-0xc(%rbp)
    1293:       7e b7                   jle    124c <main+0xc7>
    1295:       0f b6 45 c7             movzbl -0x39(%rbp),%eax
    1299:       88 45 ff                mov    %al,-0x1(%rbp)
    129c:       0f be 45 ff             movsbl -0x1(%rbp),%eax
    12a0:       48 8b 55 e0             mov    -0x20(%rbp),%rdx
    12a4:       48 89 d6                mov    %rdx,%rsi
    12a7:       89 c7                   mov    %eax,%edi
    12a9:       e8 b2 fd ff ff          callq  1060 <fputc@plt>
    12ae:       48 8b 45 e0             mov    -0x20(%rbp),%rax
    12b2:       48 89 c7                mov    %rax,%rdi
    12b5:       e8 96 fd ff ff          callq  1050 <fclose@plt>
    12ba:       48 8b 45 e8             mov    -0x18(%rbp),%rax
    12be:       48 89 c7                mov    %rax,%rdi
    12c1:       e8 8a fd ff ff          callq  1050 <fclose@plt>
    12c6:       90                      nop
    12c7:       c9                      leaveq 
    12c8:       c3                      retq   
    12c9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)