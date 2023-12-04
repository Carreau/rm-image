from flask import Flask, render_template
from random import shuffle
import os


app = Flask(__name__)

@app.route("/")
def index():
    order = list("1234")
    shuffle(order)
    return render_template("index.html", order=order)


@app.route("/image/<int:image_id>")
def display_image(image_id):
    # Logic to determine the image URL based on image_id
    image_url = f"/static/images/image{image_id}.jpg"

    return render_template("image_page.html", image_url=image_url, im=image_id)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
