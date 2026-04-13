from flask import Flask, request

app = Flask(__name__)
messages = []

# --- new part of the code ---
@app.after_request
def add_ngrok_header(responce):
    responce.headers['ngrok-skip-browser-warning']='true'
    return responce

@app.route("/")
def home():
    html = "<h1>Message Board</h1>"

    for m in messages:
        html += "<p><b>" + m["name"] + ":</b>" + m["text"] + "</p>"

    html += '''
    <form method="post" action="/submit">
        <input name="name" placeholder="Your Name"><br>
        <textarea name="message" placeholder="Your message"></textarea><br>
        <button type="submit">Submit</button>
    </form>
    '''

    return html

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    text = request.form["message"]
    messages.append({"name": name, "text": text})
    return "message received! <br> <a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)