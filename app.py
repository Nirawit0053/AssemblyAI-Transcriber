import assemblyai as aai
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

aai.settings.api_key = "8676fae4821e46e88952da5563a89101"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('result.html', transcript=transcript.text)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)