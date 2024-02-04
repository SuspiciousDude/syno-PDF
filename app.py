from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return "No file part"
    
    pdf_file = request.files['pdf_file']

    if pdf_file.filename == '':
        return "No selected file"

    if pdf_file:
        pdf_file.save(os.path.join('static/uploads', pdf_file.filename))
        src = f'uploads/{pdf_file.filename}'
        return render_template('result.html', src=src)

if __name__ == '__main__':
    app.run(debug=True)