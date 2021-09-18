# crypto/ReallynotSecureAlgorithm

>crypto/ReallynotSecureAlgorithm

> Points\
>Here's the obligatory problem!!!

***

Given p, q, e, c, it is fairly trivial to solve this question.

Using my growing python RSA code, (see in solution.py), I ran
```python
print(bytes.fromhex(hex(DecryptCEPQ(c, e, p, q))[2:]))
```

which gave the desired flag

```
flag{n0t_to0_h4rd_rIt3_19290453}
```
