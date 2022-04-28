import socket
from dataaccess_layer import check_file, count_words

if __name__ == "__main__":
    HOST = ""
    PORT = 5001
    NUM_CLIENTS = 5

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        HOST = socket.gethostbyname(socket.gethostname())
        print(HOST, socket.gethostname())
        serverSocket.bind((HOST, PORT))     #liga atraves do endereco informado em host e port
        serverSocket.listen(NUM_CLIENTS)    #para futuramente poder ter mais de 1 cliente

        while True:
            print(f"SERVER - waiting for client connection")
            clientSocket, address = serverSocket.accept()   #realiza conexao com cliente

            with clientSocket:
                while True:
                    messageReceived = clientSocket.recv(1024).decode()   #recebo mensagem do cliente com nome do arquivo
                    if not messageReceived:
                        break
                    print(f"SERVER - Message received")
                    #processamento
                    f,answer = check_file(messageReceived)  #checa se arquivo existe
                    if answer:  #se existe conta as palavras
                        msg = count_words(f)
                        clientSocket.send(bytes(msg, 'utf8'))
                    #se não existe envio mensagem de erro no nome do arquivo de volta
                    else:
                        msg = 'erro - file not found'
                        clientSocket.send(bytes(msg, 'utf8'))
                
                print("SERVER - Client closed connection")