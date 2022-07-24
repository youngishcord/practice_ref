from http import client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 12345))
print("connected")
while True:
    
    client.send(input().encode("utf-8"))