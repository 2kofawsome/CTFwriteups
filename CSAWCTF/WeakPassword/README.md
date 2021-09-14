# misc/Weak Password

>misc/Weak Password

>50 Points\
>Can you crack Aaron’s password hash? He seems to like simple passwords. I’m sure he’ll use his name and birthday in it. Hint: Aaron writes important dates as YYYYMMDD rather than YYYY-MM-DD or any other special character separator. Once you crack the password, prepend it with flag{ and append it with } to submit the flag with our standard format. Hash: 7f4986da7d7b52fa81f98278e6ec9dcb.\
>Author: moat, Pacific Northwest National Laboratory

***

Using https://hashes.com/en/tools/hash_identifier on the hash, this looks like a MD5 hash

As John the Ripper seemed confusing, I wrote up a quick python script to solve this challenge (solution.py)

Running through some dates, it gives the output
```
1
19800321
```

which corresponds to the desired flag,
```
flag{Aaron19800321}
```
