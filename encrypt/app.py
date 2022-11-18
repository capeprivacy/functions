import json
import socket

def cape_handler(raw):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect('../rpc.sock')
    sock.sendall(json.dumps(({"id": 1, "method": "CapeEncryptRPC.Encrypt", "params": [raw.decode('utf-8')]})).encode())

    response = json.loads(sock.recv(4096))
    return response['result']