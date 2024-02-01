import socket

target_host = "arielahomecare.co.uk"
target_port = 80

# create a socket object client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to client
client.connect((target_host,target_port))

#sent to data
client.send(b"GET / HTTP/1.1\r\nHost: arielahomecare.co.uk\r\n\r\n")

#receive some date
response = client.recv(4096)

print(response.decode())
client.close()