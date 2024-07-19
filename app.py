from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'files'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            return f"فایل در مسیر {filepath} ذخیره شد."
        elif 'text' in request.form and request.form['text'].strip() != '':
            text = request.form['text'].strip()
            with open('text_input.txt', 'w') as f:
                f.write(text)
            return "متن در فایل text_input.txt ذخیره شد و به کلیپبورد کپی شد."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
