#! python3.6

import pyperclip



nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for x in nums:
    string = ""
    for n in range(32):
        string += str(x)
    print(string)

    result = input()[22:]
    pyperclip.copy(result)

print("sleep now")
