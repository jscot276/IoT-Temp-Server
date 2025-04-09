import socket, json
HOST = 'localhost'
PORT = 5000
msg = {"suggested_temperature": 22}
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(json.dumps(msg).encode())
    data = s.recv(1024)
    print("Response:", json.loads(data.decode()))