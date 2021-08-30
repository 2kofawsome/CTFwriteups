# From flag.enc
c = ["10000100100", "10010000010", "10010001010", "10000100100", "10010010010", "10001000000", "10100000000", "10000100010", "00101010000", "10010010000", "00101001010", "10000101000", "10000010010", "00101010000", "10010000000", "10000101000", "10000010010", "10001000000", "00101000100", "10000100010", "10010000100", "00010101010", "00101000100", "00101000100", "00101001010", "10000101000", "10100000100", "00000100100"]

# Code taken from enc.py
fib = [1, 1]
for i in range(2, 11):
	fib.append(fib[i - 1] + fib[i - 2])

def c2f(c):
	n = ord(c)
	b = ''
	for i in range(10, -1, -1):
		if n >= fib[i]:
			n -= fib[i]
			b += '1'
		else:
			b += '0'
	return b

# Solution,
# Finds the char at that index that results in the proper associated c[i] value
import string

i = 0
for i in range(len(c)):
	for s in string.printable:
		if (c2f(s) == c[i]):
			print(s, end = '')
			i += 1
			break
		else:
			continue
            
