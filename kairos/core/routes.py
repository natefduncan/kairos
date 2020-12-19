from kairos.utils.decorators import login_required
from flask import Blueprint, render_template
from flask import current_app as app

bp = Blueprint(
    "core",
    __name__,
    template_folder="templates",
)

@bp.route("/", methods=["GET"])
@login_required()
def home():
    return render_template("home.html")

@bp.route('/dashboard', methods=["GET"])
@login_required()
def dashboard():
    return render_template("dashboard.html")

@bp.route('/maps', methods=["GET"])
@login_required()
def maps():
    return render_template("maps.html")

@bp.route('/orders', methods=["GET"])
@login_required()
def orders():
    return render_template("orders.html")