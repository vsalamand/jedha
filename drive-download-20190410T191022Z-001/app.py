from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/merci", methods= ["GET", "POST"])
def merci():
    if request.method == "POST":
        name = dict(request.form)["nom_utilisateur"]
        email = dict(request.form)["email_utilisateur"]
        projet = dict(request.form)["message_utilisateur"]
    elif request.method == "GET":
        name = ''

    return render_template("merci.html", name = name)





if __name__ == "__main__":
    app.run(debug=True)
