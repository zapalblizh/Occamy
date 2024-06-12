import os
import PIL
import json
import base64
import math
from PIL import Image
from flask import Flask, jsonify, send_file, request, redirect, render_template, url_for
from pprint import pp
from io import BytesIO
from werkzeug.utils import secure_filename

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

def format_file_size(size_in_bytes):
    if size_in_bytes == 0:
        return "0 bytes"
    size_name = ("bytes", "KB", "MB")
    i = int(math.floor(math.log(max(size_in_bytes, 1), 1024)))
    p = math.pow(1024, i)
    size = round(size_in_bytes / p, 2)
    return f"{size} {size_name[i]}"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.files['file']

    dataPath = os.path.join(app.config['UPLOAD_FOLDER'], data.filename)

    data.save(dataPath)

    if data and os.path.getsize(dataPath) <= 10*1024*1024:  # max 10 MB
        originalSize = os.path.getsize(dataPath)
        upload_file_size = format_file_size(originalSize)
    else:
        # TODO: add a reset to the form's data if this occurs
        return jsonify(error="File size exceeds 15MB"), 413

    file_ext = os.path.splitext(dataPath)[1]

    with Image.open(dataPath) as compressed_image:
        compressedName = 'compressed-image' + file_ext

        compressedPath = os.path.join(os.path.join(os.getcwd(), "app/static/images/compressed"), compressedName)

        compressed_image.save(compressedPath, quality=20, optimize=True)

        with Image.open(compressedPath) as compressed_image:

            compressedSize = os.path.getsize(compressedPath)
            compressed_file_size = format_file_size(compressedSize)

            percentage = int((originalSize - compressedSize) / originalSize * 100)

            buffered = BytesIO()
            compressed_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue())

            return jsonify({
                'image': img_str.decode('utf-8'),
                'previewSize': upload_file_size,
                'compressedSize': compressed_file_size,
                'percentage': percentage,
                'filename': compressedName
            }), 200

    return '', 204

@app.route('/download/<filename>')
def download_file(filename):
    return send_file('/app/static/images/compressed/'+filename, as_attachment=True)