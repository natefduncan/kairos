from flask import Blueprint, render_template, redirect, url_for, request
from flask import current_app as app
from kairos.utils.objects import Token
from kairos.api.models import db, User
from argon2 import PasswordHasher
import traceback

bp = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
)

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.form.to_dict()
        if data.get("password1"):
            if data.get("password1") == data.get("password2"):
                password_hash = PasswordHasher().hash(data.get("password1"))
                data.pop("password1", None)
                data.pop("password2", None)
                data["password_hash"] = password_hash
                exists = User.query.filter_by(email=data.get("email")).scalar() is not None
                if not exists:
                    user = User(**data)
                    db.session.add(user)
                    db.session.commit()
                else:
                    return render_template("signup.html", message="Email already in use.")
            else:
                return render_template("signup.html", message="Passwords don't match.")
        else:
            return render_template("signup.html", message="Must enter a password.")
        return redirect(url_for("auth.signup"))
    else:
        return render_template("signup.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form.to_dict()
        user = User.query.filter_by(email=data.get("email")).first()
        if user:
            try:
                PasswordHasher().verify(user.password_hash, data.get("password"))
                token = Token.create_access_token({"id" : user.id})
                response = redirect(url_for("core.home"))
                response.set_cookie(key="token", value=token)
                return response 
            except Exception as e:
                traceback.print_exc()
                return render_template("login.html", message="Password or email is incorrect.")
        else:
            return render_template("login.html", message="User does not exist.")
    else:
        return render_template("login.html")

@bp.route("/logout", methods=["GET", "POST"])
def logout():
    return redirect(url_for("login"))