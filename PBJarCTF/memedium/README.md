# forens/memedium

>forens/memedium

>326 Points\
>not memeasy not memhard... just memedium. (p.s. it'd be good if you found password and wrapped it in flag{} lol)

***

## The .vmen file is not kept due to size, sorry!

Following https://www.aldeid.com/wiki/Volatility/Retrieve-password exactly,

```
volatility -f mememachinememory.vmem imageinfo
volatility -f mememachinememory.vmem --profile=WinXPSP2x86 hivelist
volatility -f mememachinememory.vmem --profile=WinXPSP2x86 hashdump -y 0xe1018370 -s 0xe161fb60 > hashes2.txt
cat hashes2.txt
```
gave the output
```
Administrator:500:cdf5e5fd95c14d936e9c218c1f22e251:31a5167ba5ce8351b0110a9d13636cd9:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
HelpAssistant:1000:2c111668e0c7fd616a8af0feb7e4fcc1:103cc84c0cbb0bada9eea387d6df8207:::
SUPPORT_388945a0:1002:aad3b435b51404eeaad3b435b51404ee:9546430bd8979312c16cb95d28bfc853:::
```

and then using https://crackstation.net/ gives
```
superman83
```

Giving the desired flag,

```
flag{superman83}
```
