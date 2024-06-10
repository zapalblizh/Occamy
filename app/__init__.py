import os
from flask import Flask, flash, request, redirect, render_template, url_for
from pprint import pp
from werkzeug.utils import secure_filename

# import abort
from werkzeug.exceptions import abort

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "app/static/images/uploads")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 15 * 1024 * 1024

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.files['file']
    data.save(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
    pp(data)
    return '', 204
