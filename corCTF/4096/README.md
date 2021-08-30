# crypto/4096

>crypto/4096

>360 Points
>I heard 4096 bit RSA is secure, so I encrypted the flag with it.

***

Taking a look source.py and output.txt, we know that
```
n = 50630448182626893495464810670525602771527685838257...
pow(m, e, n) = 156406298972120895391457696256321891254...
```

and note that n is the product of 128 primes, all of which are relatively small (2^32)
Thus, use https://www.alpertron.com.ar/ECM.HTM to find the 128 prime factors of note
Note that this may have to be used multiple times, as it soemtimes gets "stuck" on medium sized primes

Now the list of primes is in solution.py, along with n, e, c
And using https://gist.github.com/jackz314/09cf253d3451f169c2dbb6bbfed73782 it can be found that

```
m = 54372504422578163821842661820992519574720094743792971271580036722643401901785509893350887232430564989
```
thus doing Decimal -> Hex with https://www.rapidtables.com/convert/number/decimal-to-hex.html

```
m = 636F726374667B746F305F6D346E795F7072316D337335355F363361656561333761366233623232667D
```
and doing Hex -> ASCII with https://www.rapidtables.com/convert/number/hex-to-ascii.html

This gives the desired flag,
```
corctf{to0_m4ny_pr1m3s55_63aeea37a6b3b22f}
```
