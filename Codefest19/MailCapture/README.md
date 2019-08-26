# Mail capture

>Mail capture

>100

>Written by: shreyansh26

>Submissions: 270

>Difficulty: Easy

>Bob got hold of this file when going through the files of the email client on his old computer. Help him find the hidden message.

***

Downloading this file returns encoded_file.

This one contains some pretty weird characters, but also begins with "begin 664 flag_encoded" and ends with "end".
This could be somethign very important to solving it!

Since "flag_encoded is" the file itself, I tried searching for "begin 664" and voila, 
a stackexchange (https://unix.stackexchange.com/questions/290702/uuencode-is-displaying-the-file-contents-in-email-body-instead-of-attaching-the) link about Uuencode.


Then a quick google search returns this (https://www.dcode.fr/uu-encoding) decoder.

Putting in the weird string of text returns the definite flag!

CodefestCTF{7h15_15_4_c001_3nc0d1n9}