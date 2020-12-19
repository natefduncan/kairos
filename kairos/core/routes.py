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
