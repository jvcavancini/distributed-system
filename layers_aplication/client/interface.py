#CLIENT
import socket

HOST = socket.gethostname()
PORT = 5001

if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect((HOST, PORT))
        print(f"CLIENT - connected to server at port {PORT} and host {HOST}")

        while True:
            msg = input("CLIENT - Send a message: (/END to finish)")    #receive message
            if (msg == '/END'): #stop message
                break
            clientSocket.send(bytes(msg, 'utf8'))   #send message to server
            receivedMessage = clientSocket.recv(1024).decode()   #receive message from server
            print(receivedMessage)    #print message

        print("CLIENT - closed conection")