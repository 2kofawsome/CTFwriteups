# web/Hack NASA With HTML Mr. Inspector Sherlock

>web/Hack NASA With HTML Mr. Inspector Sherlock

> Points\
>now introducing... the world's best website ever!!! Link: http://147.182.172.217:42006/ . Hint: DefyGG HATES scavenger hunts...he hates them! I don't expect you to waste a perfectly good day looking through hundreds of files. Speaking of stuff hes mad about, a while ago he was carrying files around school, he tripped and he scraped his knee. Ouch!


***

Given the site http://147.182.172.217:42006/, its time to start exploring.

I kept track of each page I visited, while reading the page scanning for flags, to make sure I don't go over the same pages twice (always following all possible links)\
The pages I ended up finding were

```
http://147.182.172.217:42006/
http://147.182.172.217:42006/tipz.html
http://147.182.172.217:42006/what.html
http://147.182.172.217:42006/old.html
http://147.182.172.217:42006/new_page_1.html
http://147.182.172.217:42006/index_htm.html
http://147.182.172.217:42006/trumpglish.html
http://147.182.172.217:42006/software.html
http://147.182.172.217:42006/fonts.html
http://147.182.172.217:42006/colors.html
```

In which http://147.182.172.217:42006/what.html had a big line 
```
Flag part 2: I_th0ugh1_sh3l0ck_w2s
```
and http://147.182.172.217:42006/ had 
```
Flag part 3: a_d3t3ct1iv3????!?!?!}
```

Now, without the first part found, it was time to start looking through files. I ctrl-u'd every known page and was going to look for "flag" in each file, but thankfully right away in http://147.182.172.217:42006/ was animate.js which contained
```
flag{wA1t_a_m1nUt3_
```

Since putting these together did not work, I tried adding in an underscore, and voila the desired flag

```
flag{wA1t_a_m1nUt3_I_th0ugh1_sh3l0ck_w2s_a_d3t3ct1iv3????!?!?!}
```
