# crypto/Gotta Decrypt Them All

>crypto/Gotta Decrypt Them All

>_ Points\
>You are stuck in another dimension while you were riding Solgaleo. You have Rotom-dex with you to contact your friends but he won't activate the GPS unless you can prove yourself to him. He is going to give you a series of phrases that only you should be able to decrypt and you have a limited amount of time to do so. Can you decrypt them all?\
>nc crypto.chal.csaw.io 5001

***

Connecting to this server gives a big jumble of dots, slashes, and dashes, looks like morse code to me.\
I started with a morse code website, and then saw another encoding, and noticed I will need to decrypt them all. So I decided its time to start scripting this.

In solution.py, I first wrote a morse code decoder,\
and then it looked to me like it could be converted to ascii, so I wrote that decoder.\
The chain continued similarily, wiht each decoding leading to a new encoding, the final order of the process can best be summarized by the comments in solution.py

```python
# given large morse code
# broken into groups or "words"
# broken into individual letters
# converted morse to the letters
# converted the words (which are each a decimal number) into ascii
# converted this now clearly base64 encoding into readable RSA
# got RSA values
# since e is small, found m by finding cube root
# converted m to string
# preformed a 13 offset ceasar cipher
```

which resulted in the desired flag,
```
flag{We're_ALrEadY_0N_0uR_waY_7HE_j0UrnEY_57aR75_70day!}
```
