import socket
from threading import Thread

SERVER = None
PORT = 8050
IP_ADDRESS = '127.0.0.1'
clients = {}

def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client.addr)

def setup():
    print("\n\t\t\t\t\t\t MUSIC SENDER\n")

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS....")

    acceptConnections()

thread = Thread(target=setup)
thread.start()