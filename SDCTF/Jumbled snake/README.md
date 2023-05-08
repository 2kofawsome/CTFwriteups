# CRYPTO/Jumbled snake

>CRYPTO/Jumbled snake (150)
>k3v1n
>92 solves / 150 points
>Can you unravel the jumbled snake?

>Attachments: print_flag.py.enc jumble.py

***

Looking at jumble.py, there is a 1-to-1 mapping from printable string to printable string, so now just need to recreate it

Given print_flag.py.enc, we know that
```
{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}
```
is in the original print_flag.py

In decoder.py, findPattern() is able to search for the `_...._....._..._....._...._..._...._` pattern where `.` is a placeholder
Thus, the above string must be at index 349


And since its python, assuming jumble.py and print_flag.py follow the same format, then
```
#! /usr/bin/env python3
```
will be at index 0 in the file

Using both of these facts, decoder.py uses translate() to get a partially translate file
```
#! /usr/bin/env python3$import base64$$coded_flag $ $c2$jd$$7$$91bl$hdj$s$$$fd$gz$3$u$2shf$$$$$$def reverse$s$:$    return $$.join$reversed$s$$$$def check$$:$    $$$$$$_$$$$_$$$_$$$$_$$$$$_$$$_$$$$$_$$$$$_$$$$$$$    asert decode_flag.__doc__ is not $one and decode_flag.__doc__.upper$$[2:45] $$ reverse$check.__doc__$$$def decode_flag$code$:$    $$${'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}$$$$    return base64.b64decode$code$.decode$$$$if __name__ $$ $__main__$:$    check$$$    print$decode_flag$coded_flag$$$
```
where `$` is a placeholder

Looking through this, a few more mappings can be found which gives the translation
```
#! /usr/bin/env python3
import base64

coded_flag = 'c2$jd$$7$$91bl$hdjNs$$$fd$gz$3Nu$2shf$=='

def reverse(s):
    return ''.join(reversed(s))

def check():
    '''$$$_$$$$_$$$_$$$$_$$$$$_$$$_N$$$$_$$$$$_$$$'''
    asert decode_flag.__doc__ is not None and decode_flag.__doc__.upper()[2:45] == reverse(check.__doc__)

def decode_flag(code):
    '''{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}'''
    return base64.b64decode(code).decode()

if __name__ == '__main__':
    check()
    print(decode_flag(coded_flag))
```
where `$` is a placeholder

It appears that `$$$_$$$$_$$$_$$$$_$$$$$_$$$_N$$$$_$$$$$_$$$` is an all capital reverse of the quick brown fox string, thus using the same pattern
```
#! /usr/bin/env python3
import base64

coded_flag = 'c2RjdGZ7VV91blJhdjNsZWRfdEgzX3NuM2shfQ=='

def reverse(s):
    return ''.join(reversed(s))

def check():
    '''GOD_YZAL_EHT_REVO_SPMUJ_XOF_NWORB_KCIUQ_EHT'''
    asert decode_flag.__doc__ is not None and decode_flag.__doc__.upper()[2:45] == reverse(check.__doc__)

def decode_flag(code):
    '''{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}'''
    return base64.b64decode(code).decode()

if __name__ == '__main__':
    check()
    print(decode_flag(coded_flag))
```

and decoding the base64
```
coded_flag = 'c2RjdGZ7VV91blJhdjN$WRfdEgzX3NuM2shfQ=='
```
gave the desired flag
```
sdctf{U_unRav3led_tH3_sn3k!}
```
