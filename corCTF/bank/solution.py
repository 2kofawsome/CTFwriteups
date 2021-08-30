from telnetlib import Telnet
tn = Telnet("crypto.be.ax", 6005)
res = tn.read_until(b"(y/n) ")
tn.write(b"y\n")
word = ""

# loops until 7 returns +
def looptop():
    global word
    while (True):
        tn.write(b"7\n")
        res = tn.read_until(b"> ")
        if (res.split(b"\n")[0] == b"The qubit measured as +"):
            break
        tn.write(b"6\n")
        res = tn.read_until(b"> ")

# loops until 7 returns -
def looptom():
    global word
    while (True):
        tn.write(b"7\n")
        res = tn.read_until(b"> ")
        if (res.split(b"\n")[0] == b"The qubit measured as -"):
            break
        tn.write(b"6\n")
        res = tn.read_until(b"> ")

def check10():
    global word
    tn.write(b"6\n")
    res = tn.read_until(b"> ")
    if (res.split(b"\n")[0] == b"The qubit measured as 0"):
        word += "0"
    elif (res.split(b"\n")[0] == b"The qubit measured as 1"):
        word += "1"
    tn.write(b"9\n")

for i in range(50):
    res = tn.read_until(b"> ")
    tn.write(b"1\n")
    res = tn.read_until(b"with:")
    tn.write((str(i) + "\n").encode())
    res = tn.read_until(b"> ")
    print(word)
    looptop() ##########
    tn.write(b"8\n")
    res = tn.read_until(b"> ")

    if (res.split(b"\n")[0] == b"Qubit successfully verified."):
        looptom() ##########
        tn.write(b"8\n")
        res = tn.read_until(b"> ")
        if (res.split(b"\n")[0] == b"Qubit successfully verified."):
            check10() ##########
        elif (res.split(b"\n")[0] == b"Incorrect qubit!"):
            tn.write(b"1\n")
            res = tn.read_until(b"> ")
            tn.write(b"8\n")
            res = tn.read_until(b"> ")
            if (res.split(b"\n")[0] == b"Qubit successfully verified."):
                check10() ##########
            elif (res.split(b"\n")[0] == b"Incorrect qubit!"):
                word += "+"
                tn.write(b"9\n")
                continue

    elif (res.split(b"\n")[0] == b"Incorrect qubit!"):
        tn.write(b"1\n")
        res = tn.read_until(b"> ")
        tn.write(b"8\n")
        res = tn.read_until(b"> ")
        if (res.split(b"\n")[0] == b"Qubit successfully verified."):
            check10() ##########
        elif (res.split(b"\n")[0] == b"Incorrect qubit!"):
            word += "-"
            tn.write(b"9\n")
            continue

print(word)

res = tn.read_until(b"> ")
tn.write(b"2\n")
res = tn.read_until(b"Enter your bill:")
tn.write((word + "\n").encode())
res = res = tn.read_until(b"}")
print(res)