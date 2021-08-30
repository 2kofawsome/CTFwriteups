# crypto/dividing_secrets

>crypto/dividing_secrets

>434 Points
>I won't give you the secret. But, I'll let you divide it.
>nc crypto.be.ax 6000

***

Running nc crypto.be.ax 6000 and looking at server.py, it can be seen that each time the program is run it generates a new, random p, g where p is a strong prime and 0 < g < p
Then the message x is encrypted, giving a unique enc each time the program is run. The user then gives 64 numbers, each of which is used to encrypt x with a defined formula

thus given
```
pow(g, x, p)
```
with unknown p, g, x and 64 instances of 
```
pow(g, x // div, p)
```
with div chosen, how can one determine x?


Note that g < p, thus g^1 % p = g 
and g, p > 0, thus g^0 % p = 1

then, note that x // div = 0 when div > x, so we will use a bisection method to determine the minimum value of div where div > x, so tehn div - 1 = x

Through some trial and error with big numbers,
```
200 * '9' > x
100 * '9' <= x
150 * '9' <= x
170 * '9' > x
160 * '9' > x
155 * '9' > x
153 * '9' <= x
154 * '9' <= x
```
we set the bounds as
```
lower = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
upper = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
```

Then using the program in solution.py, it does bisection to move towards the desired div value
Note that the program quits after 64 attempts, thus these printed values are put in as the new upper and lower bounds
This ended up resulting in
```
div = x = 5207851285831991069018664616693415824195562260751582516097806772363284738507980478829791747964096025668757404599258689372930479386523996608148861164794493
```

thus doing Decimal -> Hex with https://www.rapidtables.com/convert/number/decimal-to-hex.html

```
m = 636F726374667B7175346472617431635F723373316475655F30725F6E30745F31735F3768335F7175337374316F6E383835323034323035316535373439327D
```
and doing Hex -> ASCII with https://www.rapidtables.com/convert/number/hex-to-ascii.html

This gives the desired flag,
```
corctf{qu4drat1c_r3s1due_0r_n0t_1s_7h3_qu3st1on8852042051e57492}
```
