word = str(input())

print(len(word))

for n in range(102):
    print(word[n*64:(n+1)*64])
