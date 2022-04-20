import socket

if __name__ == "__main__":
    HOST = ""
    PORT = 5001
    CON_TIMEOUT = 15
    NUM_CLIENTS = 5

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        HOST = socket.gethostbyname(socket.gethostname())
        print(HOST, socket.gethostname())
        serverSocket.bind((HOST, PORT))
        serverSocket.listen(NUM_CLIENTS)

        while True:
            # waits for first connection
            print(f"SERVER - waiting for client connection. Timeout in {CON_TIMEOUT} seconds")
            serverSocket.settimeout(CON_TIMEOUT)
            clientSocket, address = serverSocket.accept()

            with clientSocket:
                print("SERVER - Connected by", address)
                while True:
                    messageReceived = clientSocket.recv(1024)
                    if not messageReceived:
                        break
                    print(f"SERVER - Message received")
                    clientSocket.send(messageReceived)
                    print("SERVER - Message sent back")
                
                print("SERVER - Client closed connection")