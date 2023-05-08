# CRYPTO/Lake of Pseudo Random Fire

>CRYPTO/Lake of Pseudo Random Fire (300)
>18lauey2 (eugene)
>64 solves / 300 points
>Greetings! You are a weary traveller, searching for a long-lost treasure - the Beacon of True Randomness. However, in your quest to obtain it, you must go through a series of rooms to get to the Beacon. In each room there are two doors - one leads you closer to the Beacon, but the other leads to Lake of Pseudo-Random Fire - your demise! Accompanying you in your journey is a high priest named Orycull. They are your only way to tell which door is which. When Orycull utters an incantation of your choosing, the doors emit different signals. The door leading you closer to the Beacon will emit a fully random signal, while the door leading you to the Lake will emit a pseudorandom signal. A clever traveller may be able to distinguish the random and pseudorandom signals and safely get to the treasure. However, be careful as Orycull can only utter so many incantations…

>game.py

>Connect via: nc prf.sdc.tf 1337

>Note: you will need the pycryptodome Python library to do the problem.


***

Looking into game.py, I'm going to need some way to determine whether random() or pseudorandom() was called.

Noticing that we have 100 oracle calls and 50 doors, we will likely call the oracle twice for each door.

And since pseudorandom() returns the concatenation of encrypting msg and decrypting the compliment of msg, 
the solution will likely be to send in the same message some different way and see if the the two oracle responses are related.

Playing with sending `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` as the oracle message, 
fromHex() in solve.py attempts to determine what the response will be if the second oracle call is the decrypted compliment of `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`

Yay, since its re-encrypted we get back the compliment of `55555555555555555555555555555555`, we have our path forward.

solve.py then uses sockets to go through each door, choosing the random door that does not return `55555555555555555555555555555555`

This gave the desired flag
```
sdctf{n07_V3rY_pS3uD0R4nD0m_a6d137}
```
