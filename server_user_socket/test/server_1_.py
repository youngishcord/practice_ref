import socket
import webbrowser
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))
print((socket.gethostbyname_ex(socket.gethostname())[-1][-1]))

server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)


        if data == 'youtube':
            webbrowser.open('https://www.youtube.com/')

        elif data == 'vpn':
            os.startfile("C:/Program Files (x86)/Outline/Outline.exe")

        else:
            print('error')
