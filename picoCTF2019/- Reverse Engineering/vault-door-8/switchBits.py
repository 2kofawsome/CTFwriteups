
binaries = ["11110100", "11000000", "10010111", "11110000", "01110111", "10010111", "11000000", "11100100", "11110000", "01110111", "10100100", "11010000", "11000101", "01110111", "11110100", "10000110", "11010000", "10100101", "01000101", "10010110", "00100111", "10110101", "01110111", "11110001", "11000001", "11010001", "10100101", "11010001", "11010010", "11010000", "10100100", "11000000"]
final = ""
for n in binaries:
    binary = list(n)

    binary[6], binary[7] = binary[7], binary[6]
    binary[2], binary[5] = binary[5], binary[2]
    binary[3], binary[4] = binary[4], binary[3]
    binary[0], binary[1] = binary[1], binary[0]

    binary[4], binary[7] = binary[7], binary[4]
    binary[5], binary[6] = binary[6], binary[5]
    binary[0], binary[3] = binary[3], binary[0]
    binary[1], binary[2] = binary[2], binary[1]

    final += "".join(binary)+" "
print(final)
