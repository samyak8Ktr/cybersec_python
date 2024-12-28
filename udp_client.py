import socket

target_host = "127.0.0.1"
target_port = 1337

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(b"Hello this is a string", (target_host,target_port))

data, addr = client_socket.recvfrom(4096)

print(data.decode())
client.close()