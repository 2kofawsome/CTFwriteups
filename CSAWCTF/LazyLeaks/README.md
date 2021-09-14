# forensics/Lazy Leaks

>forensics/Lazy Leaks

>50 Points\
>Someone at a company was supposedly using an unsecured communication channel. A dump of company communications was created to find any sensitive info leaks. See if you can find anything suspicious or concerning.\
>Author: Andrew Prajogi


***

Opening the Lazy_Leaks.pcapng file in Wireshark, there is a lot of stuff

But this can quickly be narrowed down by using the find button, searching through "packet bytes" for "flag"

which results in the desired flag,
```
flag{T00_L@ZY_4_$3CUR1TY}
```
