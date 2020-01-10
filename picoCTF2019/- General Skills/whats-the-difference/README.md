# AUR

whats-the-difference - Points: 200 - (Solves: 309)General Skills - Unsolved
Solve
Hints
Can you spot the difference? kitters cattos. They are also available at /problems/whats-the-difference_4_1adf999793b9a8fa108ea055e81f5537 on the shell server
How do you find the difference between two files?
Dumping the data from a hex editor may make it easier to compare.

***

cd /problems/whats-the-difference_4_a78c3edce997c0d2287a41259cb9182c

cat cattos.jpg | xxd -p > ~/cattos.txt
cat kitters.jpg | xxd -p > ~/kitters.txt

diff ~/cattos.txt ~/kitters.txt

picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}