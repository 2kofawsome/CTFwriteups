# REVENGE/Open Sesame

>REVENGE/Open Sesame (100)
>k3v1n
>45 solves / 100 points
>Enter the magic words to get the flag!

>Attachments: sesame.pyc

***

In an attempt to decompile sesame.pyc, using decompyle3 from https://stackoverflow.com/questions/5287253/is-it-possible-to-decompile-a-compiled-pyc-file-into-a-py-file gave sesame.py

and https://www.toolnb.com/tools-lang-en/pyc.html gave something pretty close to gencave() from solve.py with only minor changes

From this point, reading the code suggests that this can be solved with some modular arithmetic.

After writing a modular arithmetic solver in solve.py, running it gives
```
sdctf{0p$n$s$sA$3_bUt$$n$l3$7Sp3aK!}
```

I'm not sure why some chars (I used $ to show them) didn't get solved, but this was enough for me to guess the remaining l337Sp3aK!
```
sdctf{0p3n_s3sAm3_bUt_1n_l337Sp3aK!}
```
