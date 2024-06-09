from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["IMAGE_UPLOADS"] = "app/static/images/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]
app.config['MAX_CONTENT_LENGTH'] = 10240

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/stash", methods=["POST"])
def stash():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("No filename")
                return redirect(request.url)
            if allowed_image(image.filename):
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
                print("Image saved")
                return redirect(request.url)
            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("index.html")