import socket, json
HOST = '0.0.0.0'
PORT = 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[TCP Broker] Listening on port 5000...")
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        msg = json.loads(data.decode())
        print("[TCP Broker] Received:", msg)
        response = {"final_temperature": msg['suggested_temperature'] + 1}
        conn.send(json.dumps(response).encode())
        print("[TCP Broker] Sent:", response)