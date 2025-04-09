import socket, json
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 6000))
print("UDP Broker is listening...")
while True:
    data, addr = sock.recvfrom(1024)
    msg = json.loads(data.decode())
    print("Received:", msg)
    response = {"final_temperature": msg['suggested_temperature'] + 1}
    sock.sendto(json.dumps(response).encode(), addr)