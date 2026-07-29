#udp_server.py
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 5000))
print("UDP Server Waiting...")
message, address = server.recvfrom(1024)
print(message.decode())
server.sendto("Hello Client".encode(), address)
server.close()
