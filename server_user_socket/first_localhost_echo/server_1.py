import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname_ex(socket.gethostname()))
s.bind(('176.124.206.46', 9090))
#socket.gethostbyname_ex(socket.gethostname())[-1][-1]
s.listen()

while True:
    client, address = s.accept()
    while True:
        data = client.recv(1024)
        print(data)
        print(data.decode())
        if not data: break
        if data.decode() == "Close" or data.decode() == "close": 
            client.send('close connection'.encode())
            print('close connection')
            s.close()
        client.send(data)

    s.close()