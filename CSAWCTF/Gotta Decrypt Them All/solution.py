from telnetlib import Telnet
from math import pow
import sys, base64

MORSE_CODE_DICT = { b'.----' : 1, b'..---' : 2, b'...--' : 3,
                    b'....-' : 4, b'.....' : 5, b'-....' : 6,
                    b'--...' : 7, b'---..' : 8, b'----.' : 9,
                    b'-----' : 0}

ASCII_DICT = { 97 : 'n', 98 : 'o', 99 : 'p', 100 : 'q', 101 : 'r', 102 : 's',
               103 : 't', 104 : 'u', 105 : 'v', 106 : 'w', 107 : 'x', 108 : 'y',
               109 : 'z', 110 : 'a', 111 : 'b', 112 : 'c', 113 : 'd', 114 : 'e',
               115 : 'f', 116 : 'g', 117 : 'h', 118 : 'i', 119 : 'j', 120 : 'k',
               121 : 'l', 122 : 'm'}

tn = Telnet("crypto.chal.csaw.io", 5001)

def decoder(code):
    # given large morse code
    code = code.split(b"/")
    # broken into groups or "words"
    for n in range(len(code)):
        code[n] = code[n].split(b" ")
    # broken into individual letters
    numbers = []
    for i in range(len(code)):
        numbers.append(0)
        for num in code[i][:-1]:
            numbers[i] = numbers[i] * 10
            numbers[i] = numbers[i] + MORSE_CODE_DICT[num]
    # converted morse to the letters
    encoded = ""
    for num in numbers:
        encoded += chr(num)
    # converted the words (which are each a decimal number) into ascii
    decoded = base64.b64decode(encoded)
    # converted this now clearly base64 encoding into readable RSA
    splited = decoded.split(b"\n")
    N = int(splited[0][3:])
    e = int(splited[1][3:])
    c = int(splited[2][3:])
    # got RSA values
    upper = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    lower = 1
    while True:
        mid = (upper + lower) // 2
        if (mid ** 3 <= c):
            lower = mid
        else:
            upper = mid
        if upper ** 3 == c:
            sol = upper
            break
        if lower ** 3 == c:
            sol = lower
            break
    # since e is small, found m by finding cube root
    converted = bytes.fromhex(hex(sol)[2:])
    # converted m to string
    ceasar = ""
    for letter in converted:
        if (letter in ASCII_DICT.keys()):
            ceasar += ASCII_DICT[letter]
        elif ((letter+32) in ASCII_DICT.keys()):
            ceasar += ASCII_DICT[letter+32].upper()
        else:
            ceasar += chr(letter)
    # preformed a 13 offset ceasar cipher
    return str.encode(ceasar)


code = tn.read_until(b">>")[69:-4]
res = decoder(code)
print(res)
tn.write(res + b"\n")

for n in range(5):
    code = tn.read_until(b">>")[43:-4]
    res = decoder(code)
    print(res)
    tn.write(res + b"\n")


output = tn.read_all()
print(output)
