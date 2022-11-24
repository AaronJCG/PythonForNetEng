import socket
import threading


def send_data(socket_tcp_client):  # def a function to send data to server
    while True:                    # while loop to send data many times
        server_data = input("\nClient> ")  # the messages that want to send
        print("wait for response...")   # when send the messages, the client should wait for the reponse
        if server_data == "exit":  # if enter 'exit', the connection will be closed
            break
        else:
            socket_tcp_client.send(server_data.encode("gbk"))  # send the messages to the server, encoded by 'uft-8'

    socket_tcp_client.close()  # close the socket


def recv_data(socket_tcp_client):  # def a function to receive data from server

    while True:
        recv_data = socket_tcp_client.recv(1024)  # receive data maximum 1024 bytes
        print("\nServer> ", recv_data.decode("gbk"))  # show the messages from the server, encoded by 'uft-8
        print("Client> ", end=" ")


def main():
    socket_tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a client socket
    server_ip = "127.0.0.1"                 # the ip address that want to connect
    server_port = 8890                      # the port that want to connect
    socket_tcp_client.connect((server_ip, server_port))  # bind ip and port
    print("Message sent to Server of Ji Chonggui 202222030", end=" ")
    # show the message if the client connect to the server

    send_tcp_data = threading.Thread(target=send_data, args=(socket_tcp_client,))
    recv_tcp_data = threading.Thread(target=recv_data, args=(socket_tcp_client,))
    # these two threads are for send and receive data
    send_tcp_data.start()
    recv_tcp_data.start()
    # start these to threads


if __name__ == '__main__':
    main()
