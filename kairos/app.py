import os

from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("CONNECTION_STRING")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["ASSETS_DEBUG"] = True

db = SQLAlchemy(app)

# Bundle JS/CSS files
css = Bundle(
    "node_modules/bulma/css/bulma.min.css", filters="cssmin", output="bundle.min.css"
)

assets = Environment(app)
assets.register("main_css", css)
css.build()


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
