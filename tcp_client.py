import socket

target_host = "127.0.0.1"
target_port = 9998

# Creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Connecting to the client
client.connect((target_host, target_port))

# Send some data
client.send(b"Hello server, client this side")

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()
