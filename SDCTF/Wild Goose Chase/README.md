# MISC/Wild Goose Chase

>MISC/Wild Goose Chase (100)
>mojeanmac (molly)
>52 solves / 100 points
>I once saw a huge military transport plane with FOUR propellors taking off over Geisel library! It was during one of my midnight walks last month on the 29th. I wonder where it was flying to? Find which US city it landed in with the format sdctf{City_State}

>Updated Example: If the destination was NYC, the format would be sdctf{NewYork_NewYork}

***

I first attempted to use https://www.flightradar24.com and https://globe.adsbexchange.com/?replay to watch the Geisel library and look for a plane matching the description.

While this proved unuseful, https://globe.adsbexchange.com should a MCAS Miramar Military airfield right beside the library, if I was a military transport plane thats where I would lift off.

Viewing the flight history for this airport on https://www.radarbox.com/data/airports/KNKX, I was not able to find that exact flight.

But there are a number of flights with a C30J (4 propellor) plane that went toBoise, Idaho.

```sdctf{Boise_Idaho}```
Sure enough, it works!
