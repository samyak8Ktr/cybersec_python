import socket
import threading

IP = "0.0.0.0"
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5) # maximum 5 Back log of connections
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # store client's socket and remote connections details
        client, address = server.accept() 
        print(f'[*]Accepted connection from {address[0]}:{address[1]}')

        # Thread object pointing to handle_client function and the client socket as an argument
        client_handler = threading.Thread(target=handle_client, args=(client,))

        #now we start the thread to handle the client connection
        client_handler.start()

    # Perform a recv() and send and ACK
def handle_client(client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode("utf-8")}')
            sock.send(b'ACK')

if __name__ == '__main__':
        main()