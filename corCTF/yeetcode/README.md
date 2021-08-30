# misc/yeetcode

>misc/yeetcode

>402 Points\
>Brush up on your coding skills and ace your next interview with YeetCode! Flag is at ./flag.txt

***

Taking a look into yeet.py, you can see the flag is loaded into "flag.txt" and put into the same epicbox that is running our code.
Note that our code is unsantized, and will run whatever we put in (inside the epicbox)

The only output to the user is how many tests have been passed, but since we can write a very simply function to always get 10/10 tests
```python
def f(a,b):
  return a+b
```
We can add additional checks that make our passed tests decrease if desired

For example
```python
def f(a,b):
  f = open('flag.txt', 'r').read()
  if (len(f)==33)):
  	return a+b
```
returns 10/10 if and only if the flag has length 33 (thus 32 characters + '\n'),
and further
```python
def f(a,b):
  f = open('flag.txt', 'r').read()
  if (f.lower().count('a') < 1)):
  	return a+b
```
returns 10/10 if and only if there are no 'a's, switching 1 for 2, 3, 4 it can be found how many of each letter
and just by them being nice, they made all chars in this string lowercase so we dont have to worry about converting to uppercase later!

The count of each char we get is
```
a = 1 
c = 3
d = 1
e = 1
f = 3
g = 2
l = 1
m = 1
n = 1
o = 1
p = 1
r = 1
t = 1
_ = 3
{ = 1
} = 1 
0 = 1
1 = 3
3 = 2
4 = 1
6 = 1
8 = 1
```

and then using a similar method
```python
i = -1

def f(a,b):
  global i
  i += 1
  f = open('flag.txt', 'r').read()
  if (f[i] == "a"):
  	return a+b
```
will return the number of 'a's in the range of \[0:10)
```python
i = -1

def f(a,b):
  global i
  i += 1
  f = open('flag.txt', 'r').read()
  if (f[i+10] == "a"):
  	return a+b
```
will return the number of 'a's in the range of \[10:20), and the same applies for +20

after finding the range a letter should be in, simple trial and error\
```python
def f(a,b):
  f = open('flag.txt', 'r').read()
  if (f[5] == "a"):
  	return a+b
```
will return 10/10 if 'a' is at index 5

This process was slowly manually repeated while watching tv (didnt bother to automate since I wasnt doing anything anyways)
 
To give the desired flag,
```
corctf{1m4g1n3_cp_g0lf_6a318dfe}
```
