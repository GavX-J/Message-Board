from flask import Flask, request, render_template

app = Flask(__name__)
messages = []

@app.route("/")
def home():
    return render_template("Message Board.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    text = request.form["message"]
    messages.append({"name": name, "text": text})
    return "message received! <br> <a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)