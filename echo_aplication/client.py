import socket


HOST = socket.gethostname()
PORT = 5001


if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect((HOST, PORT))
        print(f"CLIENT - connected to server at port {PORT} and host {HOST}")

        while True:
            msg = input("CLIENT - Send a message: ")
            if (msg == '/END'):
                break
            clientSocket.send(bytes(msg, 'utf8'))
            print("CLIENT - Message delivered")
            receivedMessage = clientSocket.recv(1024)
            print(
                f"echo from server: {str(receivedMessage, 'utf8')}")

        print("CLIENT - closed conection")
