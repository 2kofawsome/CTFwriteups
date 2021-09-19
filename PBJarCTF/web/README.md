# rev/web

>rev/web

> Points\
>I downloaded this program back when the version number was still v1. It's been a long time... I heard the most recent update has the flag in it. Download: http://147.182.172.217:42100/v1

***

Downloading v1 running
```
strings v1
```
showed a link to v2, which had a link to v3, and I assume this continued

The way to find the final version will be to find an upper bound (where version does not exist) and then binary search for the last one

Thankfully
```
wget http://147.182.172.217:42100/v1000000000
```
returns a different length when the version number is too high (17),

Now instead of binary search, I manually did binary search for each digit in the version number while watching youtube

Which lead to
```
wget http://147.182.172.217:42100/v133791021
```

and then
```
strings v133791021 | grep "flag"
```
gave the desired flag
```
flag{h0w_l0ng_wher3_y0u_g0ne_f0r_3910512832}
```
