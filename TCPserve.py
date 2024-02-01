import socket
import threading

IP = 'https//:arielahomecare.co.uk'
PORT = 445

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((IP, PORT))
        server.listen(5)
        print(f'[*] Listening on {IP}:{PORT}')

        while True:
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            client_thread = threading.Thread(target=handle_client, args=(client,))
            client_thread.start()

    except socket.error as e:
        print(f"[-] Error: {e}")

    finally:
        server.close()

def handle_client(client_socket):
    with client_socket:
        request = client_socket.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        client_socket.sendall(b'ack')

if __name__ == '__main__':
    main()
