# pwn/walkthrough

>pwn/walkthrough

> Points\
>This program is supposed to be an introduction to pwn that guides you through creating some exploits. While the program may look long, the majority of the program is just printing information to help teach you basic pwn techniques. I hope this can help people who are confused begin to understand the general concept of how pwn exploits work by changing parts of memory. Connect with "nc 147.182.172.217 42001".

***

This program had a great tutorial for pwning inside it!

Using the solution.py script I got past the first part, then just tried 
```
%1$llx
%2$llx
%3$llx
...
```
until I was able to understand wehre I was on the stack, giving me '573daedc' as the number

So with https://www.rapidtables.com/convert/number/hex-to-decimal.html I inputted 1463660252

Giving the desired flag,

```
flag{4nd_s0_th3_3xpl01ts_b3g1n}
```
