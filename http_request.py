from flask import Flask, request, render_template
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/send_request', methods=['POST'])
def send_request():
    url = request.form.get('url')
    user_agent = request.form.get('user_agent')
    headers = {'User-Agent': user_agent}
    data = request.form.get('data')
    method = request.form.get('method')

    if method == 'GET':
        response = requests.get(url, headers=headers, data=data)
    elif method == 'POST':
        response = requests.post(url, headers=headers, data=data)
    elif method == 'PUT':
        response = requests.put(url, headers=headers, data=data)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers, data=data)
    elif method == 'HEAD':
        response = requests.head(url, headers=headers, data=data)
    else:
        return 'Invalid method', 400

    return response.text

if __name__ == '__main__':
    app.run(port=5000)
