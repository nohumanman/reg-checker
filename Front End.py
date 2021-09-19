from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/front-end")
def front_end():
    return render_template("Photos.html")


@app.route("/unprocessed.png")
def unprocessed_png():
    return send_file("Test.jpg")


@app.route("/Results.jpg")
def processed_png():
    return send_file("Result.jpg")


app.run(host="0.0.0.0", port=8090)
