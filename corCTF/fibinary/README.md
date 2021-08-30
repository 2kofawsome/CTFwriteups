# crypto/fibinary

>crypto/fibinary

>205 Points\
>Warmup your crypto skills with the superior number system!

***

Taking a look enc.py and flag.enc, it becomes clear that this c2f(c) function operates on each c independantly, thus the index of a character is irrelevant to what its associated 10001000... value will be.
Thus, we can loop through all possible ASCII characters and check if they would output the 1001... for any index in flag.enc.

This was done in solution.py

This gives the desired flag,
```
corctf{b4s3d_4nd_f1bp!113d}
```
