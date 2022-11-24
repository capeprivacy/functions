import json
import socket

def cape_handler(raw):
    payload = json.loads(raw.decode('utf-8'))

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect('../rpc.sock')
    sock.sendall(json.dumps(({"id": 1, "method": "CapeEncryptRPC.Decrypt", "params": [payload["data"]]})).encode())

    response = json.loads(sock.recv(4096))
    return response