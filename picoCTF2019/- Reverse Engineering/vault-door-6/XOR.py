

inters = "59 101 33 10 56 0 54 29 10 61 97 39 17 102 39 10 33 29 97 59 10 45 101 39 10 54 100 97 98 51 103 54"
listers = inters.split(" ")
print(listers)

finals = ""
for n in listers:
    finals += str(int(n) ^ 85) + " "

print(finals)
    
