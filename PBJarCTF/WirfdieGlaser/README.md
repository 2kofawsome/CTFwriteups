# forens/Wirf die Gläser an die Wand

>forens/Wirf die Gläser an die Wand

>361 Points\
>Our operatives managed to intercept this message. We know they've been transporting their plans over the network we infiltrated so there must be something here that we're not seeing.

***

Opening this file, there was some weird white spacing at the end of each line.

Since I wasn not able to make out any binary in it,
I used http://manpages.ubuntu.com/manpages/bionic/man1/stegsnow.1.html

with the command
```
stegsnow message.txt
```

Sadly this did not work, so I started playing around with possible apsswords and toggling compression

Nothing in the title of the challenge seemed to be the password,\
so I used variations of title of the song (googled the lyrics in message.txt) and finally came across
```
stegsnow -C -p "Moskau" message.txt
```

Giving the desired flag,

```
flag{du_bist_ein_echter_Russe}
```
