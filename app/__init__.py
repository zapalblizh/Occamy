import os
import PIL
from PIL import Image
from flask import Flask, flash, request, redirect, render_template, url_for
from pprint import pp
from werkzeug.utils import secure_filename

# import abort
from werkzeug.exceptions import abort

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "app/static/images/uploads")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(os.path.join(os.getcwd(), "app/static/images/compressed")):
    os.makedirs(os.path.join(os.getcwd(), "app/static/images/compressed"))

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 15 * 1024 * 1024

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.files['file']
    dataPath = os.path.join(app.config['UPLOAD_FOLDER'], data.filename)

    data.save(dataPath)

    file_ext = os.path.splitext(dataPath)[1]

    with Image.open(dataPath) as compressed_image:
        image_height = compressed_image.height
        image_width = compressed_image.width

        compressedName = 'compressed-image' + file_ext

        print("The original size of Image is: ", round(len(compressed_image.fp.read())/1024,2), "KB")

        compressedPath = os.path.join(os.path.join(os.getcwd(), "app/static/images/compressed"), compressedName)

        compressed_image.save(compressedPath, quality=20, optimize=True)

        with Image.open(compressedPath) as compressed_image:
            print("The compressed size of Image is: ", round(len(compressed_image.fp.read())/1024,2), "KB")

    return '', 204
