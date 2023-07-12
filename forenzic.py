import socket


def check_port(port: int) -> bool:
    opened = False
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(5)
        sock.close()
    except socket.error as e:
        pass
    else:
        opened = True
    return opened


with open('ports.txt', 'w') as f:
    for i in range(1024, 1030):
        f.write(f' Port {i} - {check_port(i)}\n')
