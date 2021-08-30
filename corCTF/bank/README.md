# crypto/bank

>crypto/bank

>489 Points
>To keep up with the latest trends CoR is introducing a quantum bank for all your secure banking needs. Unfortunately no one on CoR actually knows how quantum computing works, least of all me...
>nc crypto.be.ax 6005

***

Taking a look at server.py and playing around on the nc, 
to get this flag I would have to find a way determine all 50 qubits created randomly at the beginning

In an attempt to find somewhere with unintended behaviour, I edited server.py to print the matrix after each cycle (line 92)
and started playing around with the server locally. I kept track of what 1, 2, 3, 4 did for various starting matrices
I tried to ignore 5 as I felt this rotation would not help with determining which of the 5 qubits it is
I confirmed that 8 verifies if the given quibet is correct when in the correct "basis", but is completely random when the given quibet is in the wrong "basis"
This is because, 6 and 7 are completely random (and used by 8). There may be some method to the madness,
but as far as I can tell I can see no way to know what the output of 6 or 7 will be when the given quibet is in the opposite "basis"

Now note that the output of 6/7 does tell you what the bottom value of the matrix is (0/1 or +/-)
And note that the possible starting matrices are \[1,0\], \[0,1\], \[sqrt, sqrt\], \[sqrt, -sqrt\]
notice something weird, the matrices in basis 01 are reverse but only the bottom value in matrices in -+ basis change
Now note that 1 switches the order of matrices

And this point I was fairly certain that I could use this information to at least determine if the matrix was \[sqrt, sqrt\]
And I assumed that this would end up leading to determining any matrix
through trial-and-error I was able to determine a process for determing which matrix it is

See the attached pdf for my semi-turing machine/flowchart of how one can determine the matrix
Note that it first determines if the matrix belongs to {\[sqrt,sqrt\], \[1,0\], \[0,1\]}, {\[sqrt,-sqrt\], \[1,0\], \[0,1\]}
and then each branch determines if +- or 01 basis
then determining if \[0,1\], \[1,0\] is trivial


Now since the bill is 50 quibets, clearly this process cannot be completed by hand each times
Check 
```solution.py```
for the code I used to run through this, 
and in the end this gives the desired flag,
```
corctf{4lw4ys_d3str0y_y0ur_f4k3s}
```
