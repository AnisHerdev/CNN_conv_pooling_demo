from flask import Flask, render_template, request
from max_pooling import convert_to_numpy, max_pooling_colored, max_pooling_black_and_white, save_image

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/convolution",methods=["GET"])
def convolution():
    return render_template("convolution.html")

@app.route("/max_pooling",methods=["GET","POST"])
def max_pooling():
    if request.method == 'POST':
        img_array = convert_to_numpy("naruto.png")
        pooled_array = max_pooling_colored(img_array)
        save_image(pooled_array,"max_pooled_flask_color.png")
    return render_template("max_pooling.html")

@app.route("/min_pooling",methods=["GET"])
def min_pooling():
    return render_template("min_pooling.html")

if __name__ == "__main__":
    app.run()