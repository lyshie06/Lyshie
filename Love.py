from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "welcome my love"
@app.route("/about")
def about():
    return "this is for you my love"
@app.route("/contact")
def contact():
    return "this is my page"
if __name__ == "__main__":
                   app.run()