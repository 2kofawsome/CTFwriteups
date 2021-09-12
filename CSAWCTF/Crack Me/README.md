# warm-up/Crack Me

>warm-up/Crack Me

>_ Points\
>Can you crack this? Your hash: a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c. Your salt: the encryption method of the hash. (So if the hash is of the word example, you would submit flag{example} to score points.) UPDATE Friday 9PM: To streamline your efforts we would like to give you some more details about the format for the hash encryption method. An example: if you think the hash is RIPEMD-128, use ripemd128 for the salt.

***

Since the hash is 64 digits, I assumed sha256, but this was confirmed with https://hashes.com/en/tools/hash_identifier

As John the Ripper seemed confusing, I wrote up a quick python script to solve this challenge (solution.py)

Running through a big list of passwords that I found, with the sha256 salt at the beginning (I also tried the end), it gives a solution!

and this gives the desired flag,
```
flag{cathouse}
```
