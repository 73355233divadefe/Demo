#import socket

#target_host = "wwww.com"
#target_port = 80

#client = socket_socket ( socket_AP_INET, socket.SOCK_STREAM)
#client_connect ((target_host , target_port))

import socket

def scan_ports("arielahomecare.co.uk", 80):
    print(f"Scanning ports on {80}...")

    for port in range(1000, 1024 + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((http://arielahomecare.co.uk, 80))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        sock.close()

if __name__ == "__main__":
    target_host = "localhost"  # Change this to the target IP or hostname
    start_port = 1
    end_port = 1024  # You can modify the range of ports to scan

    scan_ports(target_host, start_port, end_port)
