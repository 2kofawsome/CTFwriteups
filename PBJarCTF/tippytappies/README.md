# forens/tippy tappies

>forens/tippy tappies

> Points\
>how'd you get this in the first place :eyes: dids you has logger on me?

***

Following https://bitvijays.github.io/LFC-Forensics.html#usb-forensics I determined that this is a USB keyboard (https://linux-hardware.org/index.php?id=usb:258a-6a88)

Then, following https://abawazeeer.medium.com/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4 I got the CSV extracted file-2412351679f4

Then with solutions.py (using the mapping of the previous link with slight adjustments)


I got,
```
flaag wowgooduusbdettectivveworrk
```
which becomes the desired flag
```
flag{wowgoodusbdetectivework}
```
