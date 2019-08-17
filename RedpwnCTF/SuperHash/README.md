# Super Hash

>Super Hash

>50

>Written by: NotDeGhost

>Does hashing something multiple times make it more secure? I sure hope so. I've hashed my secret ten times with md5! Hopefully this makes up for the fact that my secret is really short. Wrap the secret in flag{}.

>Note: Follow the format of the provided hash exactly

>Hash: CD04302CBBD2E0EB259F53FAC7C57EE2

***

My first thought, "it sure doesnt, but it might make it worse!" so I started googling whether multiple md5 encryptions cause any errors or vunrabilities,
sadly, I found nothing. But what I did find was a lot of people saying it sure does not make it more secure.

Next I decided that since the "secret is really short", chances are I can brute force this with my favorite programming language, Python!

I wrote this code first:

```Python
import hashlib, time, string

alphabet = list(string.printable)


start = time.time()
for a in alphabet:
    hashed = a
    for n in range(10):
        hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest()
    if hashed == "CD04302CBBD2E0EB259F53FAC7C57EE2".lower():
        print(a)
print(time.time()-start)


start = time.time()
for a in alphabet:
    for b in alphabet:
        hashed = a+b
        for n in range(10):
            hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest()
        if hashed == "CD04302CBBD2E0EB259F53FAC7C57EE2".lower():
            print(a+b)
print(time.time()-start)

```

It does md5 on each string in the alphabet (which is all ACSII printable charaters), then does md5 on the md5 hash, 10 times
But sadly after getting a+b+c+d it still did not give any solution!

But then I realised that I have to 'Follow the format of the provided hash exactly', which is all caps!
Even though md5 hashes are lowercase, I need to make them uppercase before hashing.

```Python
for n in range(10):
	hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest().upper()
if hashed == "CD04302CBBD2E0EB259F53FAC7C57EE2":
```

lower() became upper() then bam, instant result when running the code, 
```
 ^
```
Which becomes flag{^}




