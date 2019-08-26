import re

file = open(".\encoded_img.txt", "r")
text = file.readlines()

findSlots = re.compile(r"""\dx\d*""", re.VERBOSE)

for m in text:
    slots = findSlots.findall(m)


    line = ""
    for n in slots:
        line += (n[0]*int(n[2:]))

    print(line)
