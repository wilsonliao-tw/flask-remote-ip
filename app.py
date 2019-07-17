from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
