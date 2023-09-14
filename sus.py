import socket

def find_unused_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
            return port
        except OSError:
            pass
    return None

start_port = 8000  # You can specify a range of ports to search within
end_port = 9000

unused_port = find_unused_port(start_port, end_port)

if unused_port:
    print(f"Found an unused port: {unused_port}")
else:
    print("No unused ports found in the specified range.")
