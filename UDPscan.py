import socket

host_target = "arielahomecare.co.uk"
port_target = 80
##create client socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##SEND SOME DATA
client.sendto(b"AAABBBCCC",(host_target,port_target))
##receive some data
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()