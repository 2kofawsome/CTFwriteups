# MISC/Fork bomb protector

>MISC/Fork bomb protector (100)
>k3v1n
>181 solves / 100 points
>We built a playground for people to try out Linux. We are tired of customer complaints about malicious fork bombs rummaging the server, hogging system resources, and bringing everything down to a crawl, so we built our own proprietary fork-bomb protector. As an "unintended" consequence of that, people cannot run commands normally. Our genius head of the engineering team suggests this to be a security "feature", not a bug, since this essentially turns our product into a restricted shell. Bye bye, RCEs!

>Attachments: nofork.py

>Connect via: socat FILE:$(tty),raw,echo=0 TCP:nofork.sdc.tf:1337

>Flag (solved)

***

From nofork.py we can't use forks of any kind, but thanks to CS350 what we can use is exec!

```exec cat flag.txt```
gave the desired flag
```
sdctf{ju5T_3xEc_UR_w4y_0ut!}
```
