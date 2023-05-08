# MISC/Secure Runner

>MISC/Secure Runner (200)
>Infernis
>70 solves / 200 points
>I made a service where people can upload C code to my server and run it! The best part is that it's completely secure! Try running the number guessing game I made :)

>Connect via cat program.c - | nc secure-runner.sdc.tf 1337

>program.c

***


Viewing program.c, nothing seems too interesting. What happens if I pipe in the wrong program though?

Copying fakeProgram.c from https://www.geeksforgeeks.org/c-program-to-read-contents-of-whole-file/, this should print out the flag.
```
cat fakeProgram.c - | nc secure-runner.sdc.tf 1337
```
with response
```
ERROR: Refusing to run file, invalid checksum (3e2df162)!
```
ah I see, I need to upload C code with a collided checksum!

First, I need to know what hash function we are using for a checksum. 

After a bit of Googling  for 32 bit hash functions, I ended up putting the same fakeProgram.c into https://emn178.github.io/online-tools/crc32.html and got 3e2df162, we found our hash function!

Using the same site to get the program.c hash, it's 38df65f2, we now need a way to create collisions

Using forcecrc32.py from https://www.nayuki.io/page/forcing-a-files-crc-to-any-value, I'm able to patch the last 4 char of fakeProgram.c

So add in a comment
```
// aaaa
``` 
and patch in the fix!


Now attempting
```
cat fakeProgram.c - | nc secure-runner.sdc.tf 1337
```
gave the desired flag
```
sdctf{n0w_th4t5_wh4t_i_ca1l_crcecurity!}
```
