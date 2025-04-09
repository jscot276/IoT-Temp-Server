from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/set-temp', methods=['POST'])
def set_temp():
    data = request.get_json()
    print("Received:", data)
    return jsonify({"final_temperature": data['suggested_temperature'] + 1})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)