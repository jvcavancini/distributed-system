import socket
import select
import sys

from dataaccess_layer import check_file, count_words

conexoes = {}

entradas = []

def atendeRequisicoes(clientSocket, address):
    messageReceived = clientSocket.recv(1024).decode()   #receive message from client with file name
    if not messageReceived:
        print(str(address) + '-> encerrou')
        entradas.remove(clientSocket)
        del conexoes(clientSocket)
        clientSocket.close()
        return
    print(f"SERVER - Message received")
    #process
    f,answer = check_file(messageReceived)  #check if file exist
    if answer:  #if exists, count the words
        msg = count_words(f)
        clientSocket.send(bytes(msg, 'utf8'))
    #if not send error message
    else:
        msg = 'erro - file not found'
        clientSocket.send(bytes(msg, 'utf8'))

if __name__ == "__main__":
    HOST = ""
    PORT = 5001
    NUM_CLIENTS = 5

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        HOST = socket.gethostbyname(socket.gethostname())
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print(HOST, socket.gethostname())
        serverSocket.bind((HOST, PORT))     #create bind through host and port
        serverSocket.listen(NUM_CLIENTS)    #so in the future I can have multiple clients

        while True:
            print(f"SERVER - waiting for client connection")
            entradas.append(sock)
            entradas.append(sys.stdin)
            r, w, e = select.select(entradas,[],[])
            for pronto in r:
                if pronto==socket:
                    clientSocket, address = serverSocket.accept()   #create connection
                    print('conectado com ', address)
                    clientSocket.setblocking(False)
                    entradas.append(clientSocket)
                    conexoes[clientSocket] = address
                elif pronto==sys.stdin:
                    cmd=input()
                    if cmd=="/END":
                        if not conexoes:
                            sock.close()
                            sys.exit()
                        else:
                            print("Ha conexoes ativas")
                else:
                    atendeRequisicoes(pronto,address)
            