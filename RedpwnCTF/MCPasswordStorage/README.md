# MC Password Storage

>MC Password Storage

>333

>Written by: Brownie

>My friend stores his passwords in Minecraft worlds, and while he was distracted, I grabbed one of them. However, the password is encrypted. Could you help me get his password?

>Note: Load the world in Minecraft Java to do the challenge

***

This was the hardest challenge I completed at 333 points, but I believe that that was likely only due to people not owning Minecraft Java.
Like me for example, I own bedrock and grew up on java/360 edition, but was not able to even try this challenge for most of the competition.
Luckly my other team member had java edition and brought over their laptop so I could attempt the problem.


First thing I notice, there is not much to this:
* There appears to be a main room with a button and a single lamp (on/off)
* A tower of sand/dragon eggs which fall with each button press
* A loop of glass/some other block which rotates on each button
* A box structure that when opened shows a redstone XOR gate


Now my redstone knowledge from building those automatic farms comes in handy, because I know eaxctly what is happening and its 11:30 on the last day of the competition.
30mins to complete the problem (they came over at 11).

The sand allows redstone through, the dragon eggs do not.

The other block (forget what) allows redstone, the glass does not

This means with every button press the 2 diffferent "functions" will return 1 or 0, and the overall XOR of those will be displayed to the lamp.
Hopefully thats binary to ASCII because we now have 20mins to finish it.

Now since I was hoping this would only be the plain normal ASCII charcters, every 8th button click must be off (0).
I went though the 11 possible wheel starting points (10100110001), and wrote down the start of the order of the tower (00001111111000010101000011000001...)
Since the first bit of tower was 0, the wheel must also start with 0, so I was able to take away 5 of the starting points.

```
1 X 
0
1 X
0
0
1 X
1 X
0
0
0
1 X
```

Then since the 9th bit of tower was 1, the wheel must start with 1 (XOR 1 and 1 = 0). See what Im doing

```
1 X 
01001100 0 X
1 X
00110001 1
01100011 0 X
1 X
1 X
00011010 0 X
00110100 1
01101001 1
1 X
```

Then since the 17th bit of tower was 0, the wheel must start with 0 again.

```
1 X 
01001100 0 X
1 X
00110001 10100110 0
01100011 0 X
1 X
1 X
00011010 0 X
00110100 11000110 1 X
01101001 10001101 0
1 X
```

Then in my haste (15 minutes left!) I made a near fatal error, I thought that the top one (00110001 10100110 0) had an X,
so I only attempted the bottom one (01101001 10001101 0). Luckly that was the right path because there was no time to spare.


I typed the 1s and 0s into a bianry to [ACSII converter](https://www.rapidtables.com/convert/number/binary-to-ascii.html), and my team member clicked the button to change the bits as quick as the redstone system updated.
Time was ticking down, knees weak, palms were sweaty, vomit on my sweater already...

Focus! No time to lose myself. It was literally 11:57 when I clicked enter on the converter.


Yes, thank heavens I did not misstype anywhere, I now have a flag. I forget the exact flag (I was too excited) but it was something like flag{m1n3cr4f7_X0R}.


11:58 when I clicked submit, the 10th problem of the CTF (10 was my goal). YES!

























