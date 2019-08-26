# Weird encoding

>Weird encoding

>200

>Written by: shreyansh26

>Submissions: 72

>Difficulty: Medium

>This encoding is supposed to represent an image. Figure out how?

***

Downloading this image returns the encoded_img file (but without .txt on the end).

Opening this file in a text editor shows that its plaintext in the form of 0x68+1x1+0x11+1x1+0x19

Considering the 1x# or 0x# for each group, and that the #s all add up to 100 on each line, I assume this is the recipy for creating an image.

For example:

```
0x5
0x2+1x1+0x2
0x1+1x1+0x1+1x1+0x1
0x2+1x1+0x2
0x5
```

Makes a Diamond!

```
00000
00100
01010
00100
00000
```



So I wrote a very small Python program to draw the picture that was described in the file (decodeImg.py)


```Python 3

import re

file = open(".\encoded_img.txt", "r")
text = file.readlines()

findSlots = re.compile(r"""\dx\d*""", re.VERBOSE)

for m in text:
    slots = findSlots.findall(m)


    line = ""
    for n in slots:
        line += (n[0]*int(n[2:]))

    print(line)
	
```



And the output is stored in "decodeImgOutput.txt"!

But it doesn tlook like an image, yet...



I used notepad++ and zoomed out (ZoomedOutImg.png), and look at that, a clear flag to input!

CodefestCTF{This_15_7h3_f14g}