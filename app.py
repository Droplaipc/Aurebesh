from flask import Flask, render_template, request, redirect, url_for
from program import traductor
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def trad():
    if request.method == "POST":
        text_spanish = request.form["text_spanish"]
        traduced_text = traductor(text_spanish)
        return redirect(url_for("Aurebesh", text= traduced_text))

    return render_template("index.html")

@app.route("/traduced")
def Aurebesh():
    text = request.args.get("text")
    return render_template("traduced.html", text = text)

if __name__ == "__main__":
    app.run(debug=True)


