# forens/Art Mystery

>forens/Art Mystery

>320 Points\
>You put your new artwork into a safe but when you looked in the morning, someone had stolen it!! Next time you'll have to cheCk youR loCk.

***

The given PNG file (art.png) was corrupted, so after some googling I used https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header and https://stackoverflow.com/questions/54845745/not-able-to-read-ihdr-chunk-of-a-png-file to determine that I need to change the IGHR width and height

Notice the CRC in the challenge description? It must be possible to extract the solution from the IDHR CRC (checksum)

Using https://stackoverflow.com/questions/42748223/python-how-to-calculate-png-crc-value, with updates to allow Python3, you can check out my code in solutions.py

Then making these changes, the file art-fixed.png was not corrupted, and the flag was in plain sight once opened!


Giving the desired flag,

```
flag{you_found_my_size!}
```
