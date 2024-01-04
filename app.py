from flask import Flask, send_file, render_template, request
import requests
import shutil
import os
import time

app = Flask(__name__)

@app.route('/download_video', methods=['POST'])
def download_video():
    video_url = request.form['video_url']
    expiry_time = int(request.form['expiry_time'])
    response = requests.get(video_url, stream=True)
    file_name = f"{time.time()}.mp4"
    with open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    @app.route('/get_video/<file_name>')
    def get_video(file_name):
        if os.path.exists(file_name) and time.time() - os.path.getmtime(file_name) < expiry_time * 3600:
            return send_file(file_name, as_attachment=True)
        else:
            return "The download link has expired."

    return render_template('download.html', download_link=f"/get_video/{file_name}")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
