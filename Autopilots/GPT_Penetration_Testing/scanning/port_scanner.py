import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"Port {port} is open.")
    except:
        print(f"Port {port} is closed.")
    finally:
        s.close()

if __name__ == "__main__": socket
    host = input("Enter host: ")
    for port in range(1, 5555):
        scan_port(host, port)
