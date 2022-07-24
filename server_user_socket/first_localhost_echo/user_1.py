import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('172.31.80.1', 2222))#127.0.0.1 #тут стоит ip сервера поднятого на ноутбуке! те в локальной сети 192.168.1.37

while True:

    out = input('Введите сообщение: ')

    sock.send(out.encode())

    encome = sock.recv(1024)

    print(encome.decode().upper())

    if encome.decode() == 'close connection':
        sock.close()