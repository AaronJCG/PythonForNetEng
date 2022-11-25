import socket
import threading
# these two libraries we used in this programme

client_flag = 'on'
'''this is the flag means that whether there is a new client connect to the server.
the server will be 'on' (default) and give a unique thread to wait for a new client
if a new client connects to the server, the state will turn to 'on' again to give
another unique thread to the new client
'''


def from_client(socket_tcp_server):
    global client_flag  # reopen the client_flag, it was 'off' when the server accepted a client

    client_socket, client_addr = socket_tcp_server.accept()
    # .accept() means that allows the server to listen the client port all the time,
    # print(self.con,">>>>>>",self.address)
    print(f"{client_addr} connected to Server "
          f"\nwaiting for response")
    '''If the server accept a client, then it will print the message, because all the client are from
    the same computer(my laptop), so the client must is mine.
    
    Then the client will waiting for the response or some messages from the client, so that the server
    can response it.
    '''

    while True:           # using while loop to make server can always receive and send messages until the client close the connection
        recv_data = client_socket.recv(1024)  # receive the data from the client, maximum 1024 bytes
        if recv_data:
            print(f"Port: {client_addr[1]} <Client> {recv_data.decode('gbk')}")
            # show the port of the client and the messages from the client
            # this program can connect many clients and can receive and send messages to each client
            # so it would be better add the 'port' to show which client sent the message
        else:
            break

        send_data = input("\nServer> ")       # input the message that want to send to client
        print("Server> wait for response...")    # server can send more messages until the client responses
        client_socket.send(send_data.encode("gbk"))    # send the input message to the client
    client_socket.close()      # close this unique socket which is connecting
    print("Client closed connection")    # show something to remind the serve                                         r


def main():
    global client_flag           # global the variable to use
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.AF_INET means that we use IPv4 (AF_INET is IPv6);
    # socket.SOCKET_STREAM means that we use TCP Protocol (SOCKET_DGRAM is UDP)
    ip = '172.20.10.5'
    port = 8891
    tcp_server.bind((ip, port))
    # bind ip and port of server.

    tcp_server.listen(3)  # maximum 4 clients can connect to this server, otherwise it will reject the client (negative).
    print("Listening for a new port...")  # show the state, this state is raised by the "accpet()" function

    client1_threading = threading.Thread(target=from_client, args=(tcp_server,))
    # Each client will be controlled in a separate thread
    client1_threading.start()
    # start this thread

    while True:
        if client_flag == 'on':
            # if the server receive the request from the client ("on"), then it will start a new thread
            client1_threading = threading.Thread(target=from_client, args=(tcp_server,))  # create a new thread
            client1_threading.start()  # start this new thread
            client_flag = 'on'
            # the "on" means that the number of thread will not increase all the time
            # only start a new thread when the server receive the request from the client


if __name__ == '__main__':   # run the program
    main()
