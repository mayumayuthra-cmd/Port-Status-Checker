import socket

def check_port(host, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED or FILTERED")

        sock.close()

    except socket.gaierror:
        print("Invalid hostname")

    except ValueError:
        print("Invalid port number")

    except Exception as e:
        print("Error:", e)


host = input("Enter IP address or hostname: ")
port = int(input("Enter port number: "))

if 1 <= port <= 65535:
    check_port(host, port)
else:
    print("Enter a valid port number (1-65535)")