from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/set-temp', methods=['POST'])
def set_temp():
    data = request.get_json()
    print("[REST Broker] Received:", data)
    response = {"final_temperature": data['suggested_temperature'] + 1}
    print("[REST Broker] Sent:", response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
