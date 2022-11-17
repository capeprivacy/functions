import json
import socket

def cape_handler(name):
    name = name.decode('utf-8')

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect('./rpc.sock')

    sock.sendall(json.dumps(({"id": 1, "method": "Greeter.Greet", "params": [name]})).encode())

    return (sock.recv(4096))