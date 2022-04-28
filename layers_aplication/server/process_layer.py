import socket
from dataaccess_layer import check_file, count_words

if __name__ == "__main__":
    HOST = ""
    PORT = 5001
    NUM_CLIENTS = 5

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        HOST = socket.gethostbyname(socket.gethostname())
        print(HOST, socket.gethostname())
        serverSocket.bind((HOST, PORT))     #create bind through host and port
        serverSocket.listen(NUM_CLIENTS)    #so in the future I can have multiple clients

        while True:
            print(f"SERVER - waiting for client connection")
            clientSocket, address = serverSocket.accept()   #create connection

            with clientSocket:
                while True:
                    messageReceived = clientSocket.recv(1024).decode()   #receive message from client with file name
                    if not messageReceived:
                        break
                    print(f"SERVER - Message received")
                    #process
                    f,answer = check_file(messageReceived)  #check if file exist
                    if answer:  #if exists count the words
                        msg = count_words(f)
                        clientSocket.send(bytes(msg, 'utf8'))
                    #if not send error message
                    else:
                        msg = 'erro - file not found'
                        clientSocket.send(bytes(msg, 'utf8'))
                
                print("SERVER - Client closed connection")