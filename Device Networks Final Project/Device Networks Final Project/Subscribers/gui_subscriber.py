import tkinter as tk
from tkinter import messagebox
import socket, json, requests

def send_request(protocol):
    try:
        suggested_temp = int(temp_entry.get())
        msg = {"suggested_temperature": suggested_temp}
        print(f"[{protocol}] Sent:", msg)

        if protocol == "TCP":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("localhost", 5000))
                s.send(json.dumps(msg).encode())
                data = s.recv(1024)
                response = json.loads(data.decode())

        elif protocol == "UDP":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(json.dumps(msg).encode(), ("localhost", 6000))
            data, _ = sock.recvfrom(1024)
            response = json.loads(data.decode())

        elif protocol == "REST":
            r = requests.post("http://localhost:7000/set-temp", json=msg)
            response = r.json()

        result_label.config(text=f"[{protocol}] Final Temperature: {response['final_temperature']}°C")
        print(f"[{protocol}] Received:", response)

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Smart Temp GUI Subscriber")
tk.Label(root, text="Enter Suggested Temperature (°C):").pack()
temp_entry = tk.Entry(root)
temp_entry.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Send via TCP", command=lambda: send_request("TCP")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Send via UDP", command=lambda: send_request("UDP")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Send via REST", command=lambda: send_request("REST")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="Final Temperature: N/A")
result_label.pack(pady=10)

root.mainloop()
