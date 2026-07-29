#udp-client.py
#udp-sock_dgram
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("Hello Server".encode(), ("localhost", 5000))
reply, address = client.recvfrom(1024)
print(reply.decode())
client.close()