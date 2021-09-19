# rev/polymer

>rev/polymer

> Points\
>I learned in my biology class that a polymer is a chain of monomers that can sometimes form long strings of molecules.

***

Opening up the provided file, I knew it was gonna be somewhere in that mess (chain?) of n0t-flags

Running the command
```
grep --text -o "flag{[^}]*}" polymer
```

gives a list (this must be the chain?) of identical n0t-flags, so
```
grep --text -o "flag{[^}]*}" polymer | uniq
```

gave the desired flag

```
flag{ju5t_4n0th3r_str1ng5_pr0bl3m_0159394921}
```
