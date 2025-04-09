import socket, json
HOST = 'localhost'
PORT = 5000
msg = {"suggested_temperature": 22}
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(json.dumps(msg).encode())
    data = s.recv(1024)
    response = json.loads(data.decode())
    print("[TCP Subscriber] Response:", response)