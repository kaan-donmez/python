from flask import Flask, render_template, request
import requests

app = Flask(__name__)

githubUrl = "https://api.github.com/users/"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        githubName = request.form.get("githubName")
        response = requests.get(githubUrl + githubName)
        userProfile = response.json()
        return render_template("index.html", userProfile=userProfile)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
