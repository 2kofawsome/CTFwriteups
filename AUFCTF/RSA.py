import pyperclip, time, pyautogui


import socket

def netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(repr(data))
    s.close()

netcat("challenges.auctf.com", "30030", "A")

print(hey)

time.sleep(1)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(1, 22):
    pyperclip.copy("auCTF{" + str("u")*x) #sw
    pyautogui.click(button='right')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(.15)

print(no)

for x in alpha:
    pyperclip.copy("auCTF{" + x*25) #r, t, u
    pyautogui.click(button='right')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(.15)

print(no)






print("auCTF{" + str("_")*50)
print("auCTF{" + str("}")*50)

for x in range(10):
    print("auCTF{" + str(x)*20)

for x in alpha:
    print("auCTF{" + x*20)
    input()


