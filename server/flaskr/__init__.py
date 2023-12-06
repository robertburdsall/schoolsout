from flask import Flask, request, jsonify

app = Flask(__name__)


# Route to handle a GET request
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({'message': 'This is a GET request'})


# Route to handle a POST request
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.json  # Assuming JSON data in the request body
    return jsonify({'message': 'This is a POST request', 'data': data})


# Route to handle both GET and POST requests
@app.route('/get_post_data', methods=['GET', 'POST'])
def get_post_data():
    if request.method == 'GET':
        return jsonify({'message': 'This is a GET request'})
    elif request.method == 'POST':
        data = request.json  # Assuming JSON data in the request body
        return jsonify({'message': 'This is a POST request', 'data': data})


if __name__ == '__main__':
    app.run(debug=True)
