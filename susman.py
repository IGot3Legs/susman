import socket

def find_free_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))  # Bind to any available IP and port 0 to get a free port
    port = sock.getsockname()[1]
    sock.close()
    return port

free_port = find_free_port()
print("Free port:", free_port)
