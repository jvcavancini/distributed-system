#CLIENTE
import socket

HOST = socket.gethostname()
PORT = 5001

if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect((HOST, PORT))
        print(f"CLIENT - connected to server at port {PORT} and host {HOST}")

        while True:
            msg = input("CLIENT - Send a message: ")    #recebi mensagem
            if (msg == '/END'): #caso queira parar
                break
            clientSocket.send(bytes(msg, 'utf8'))   #enviei mensagem
            receivedMessage = clientSocket.recv(1024)   #recebi mensagem do servidor
            print(
                f"echo from server: {str(receivedMessage, 'utf8')}")    #depois mudo para imprimir resposta

        print("CLIENT - closed conection")