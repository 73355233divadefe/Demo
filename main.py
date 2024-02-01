# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import socket
import threading

IP = '192.185.158.13'
PORT = 80

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()
def handle_client(client_socket):
    with client_socket:
        request = client_socket.recv(1024)
        print(f'[] Received: {request.decode("utf-8")}')
        client_socket.sendall(b'ack')
if __name__  == '__main__':
    main()