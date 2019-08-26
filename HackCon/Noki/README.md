# Noki

>Noki

>198

>I was told Vigenère Cipher is secure as long as length(key) == length(message). So I did just that! 
>Break this: g4iu{ocs_oaeiiamqqi_qk_moam!}e0gi

***

I love a good cipher, lets get right into it!!!

So this cipher is the same length as the message, thats a OTP (one time pad) and it's impossibel to crack when done right.
So I just need to find out what they did wrong.


I went to my favorite cipher site [here](https://www.dcode.fr/vigenere-cipher) and started playing around to try to solve thsi thing.


Since we know that it starts with d4rk and ends with c0de, lets try to find what letters will solve that and see if any full words can be created from it.
Such as if we figured out "Now t____ a CTF" it might be "Now thats a CTF".


But look at that, the letters that make d4rk{_________________}c0de are drk_______________cde. Does that mean what I thing it means!
Not only does length(key) == length(message), but key == message.


Thats means we can do trial and error to find which keys produce the same letters in the message


Going through the whole alphabet with keys such as "aaaaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbb", and "ccccccccccccccccccccccc"
we can determine in which locations the key of a makes an a, in which the key of b makes b, and so on and so forth.


but going through every letter returns
```
d4rk{hbj_haceeagiie_if_ghag!}c0de
```

There is defintily something wrong here, oh wait! Its because both the first half of the alphabet, and the second half will return valid letters,
so doing it again with secodn half I get
```
d4rk{uow_unprrntvvr_vs_tunt!}c0de
```

Now thats promosing, now I just have to go through and figure out which letters make readable words

```
d4rk{@@@_@@@@@@@@@@_@@_@@@@!}c0de
```
becomes...
```
d4rk{how_@@@@@@@@@@_@@_@@@@!}c0de
```
becomes...
```
d4rk{how_@@@@@@@@@@_is_@@@@!}c0de
```
becomes...
```
d4rk{how_@@@@@@@@@@_is_that!}c0de
```


But I have no idea what that middle word is.


I wrote a quick script on the Python interpreter to show all the possibilities (noki.py)
and very quickly one popped out at me, "uncreative"



So the flag must be:
d4rk{how_uncreative_is_that!}c0de