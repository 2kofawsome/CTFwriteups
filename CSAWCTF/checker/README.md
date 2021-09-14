# warm-up/checker

>warm-up/checker

>25 Points\
>What's up with all the zeros and ones? Where are my letters and numbers? (This is a reversing challenge.)

***

Taking a look checker.py, we can see that the encoding performs a series of changes to the original flag string (up, right, left, down)

Note that each of these changes has no random or unknown elements other than the string, thus they can be reversed

This reversing was implemented in solution.py, note that

```python
encoded = encoded[::-1]
encoded = right(encoded, d)
encoded = down(encoded)
encoded = right(encoded,len(encoded)-d)
```

reverses the left, down, right (where right and left swaps reverse each other)

now with the encoded string that is the result of up(plain), 
since each char returns a different string of the same length in the up() function,
we can loop through these resulting strings and find the combination that creates the desired encoded string

Again, view this in solution.py

This gives the desired flag,
```
flag{r3vers!nG_w@rm_Up}
```
