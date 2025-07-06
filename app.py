from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Asana handshake
    if 'X-Hook-Secret' in request.headers:
        return '', 200, {'X-Hook-Secret': request.headers['X-Hook-Secret']}
    # Print webhook payload
    print(request.json)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
