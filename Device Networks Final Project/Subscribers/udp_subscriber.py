import socket, json
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = {"suggested_temperature": 22}
sock.sendto(json.dumps(message).encode(), ("localhost", 6000))
data, _ = sock.recvfrom(1024)
print("Response:", json.loads(data.decode()))