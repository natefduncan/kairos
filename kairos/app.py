import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("CONNECTION_STRING")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "SECRET_KEY"

db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def home():
    return "200"

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)

