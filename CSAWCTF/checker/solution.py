def up(x):
    x = [f"{ord(x[i]) << 1:08b}" for i in range(len(x))]
    return ''.join(x)

d = 24

encoded = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"

encoded = encoded[::-1]
encoded = right(encoded, d)
encoded = down(encoded)
encoded = right(encoded,len(encoded)-d)

import string
sol = ""
encoding = ""
while encoding != encoded:
    for s in string.printable:
        tmp = (encoding + up(s))
        if tmp == encoded[:len(tmp)]:
            encoding = tmp
            sol += s
            break
print(sol)
