# forensics/LunaGuesser

>forensics/LunaGuesser

> Points\
>We intercepted this message being sent from a strange location. Can you figure out where it's being sent from? Note: The flag is the name of a location. All lowercase letters and words separated by spaces. ex: flag{new_york_city}


***

Remembering a past problem in PicoCTF 2019 that talked about moon landing information in a wav file, I assumed I would have to use similar stuff to solve this one

So I ran qsstv, ran the audio file, and got the R36_20210919_040953.png image

Well clearly this is the moon, but these flags don't work
```
flag{moon}
flag{lune}
flag{luna}
flag{space}
flag{sea_of_tranquility}
flag{tranquility_base}
flag{tranquility}
flag{tranquility_sea}
flag{tranquility_base_mare}
flag{tranquility_sea_mare}
...
```

Finally, after a few dozen attempts I got the desired flag
```
flag{mare_tranquillitatis}
```
