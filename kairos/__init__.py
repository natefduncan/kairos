from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Bundle, Environment

from kairos.api.models import db

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Development")

    db.init_app(app)
    assets = Environment(app)

    with app.app_context():
        from .auth.routes import bp as auth_bp
        from .core.routes import bp as core_bp

        app.register_blueprint(core_bp, url_prefix="/")
        app.register_blueprint(auth_bp,url_prefix="/auth")
        db.create_all()

        if app.config["FLASK_ENV"] == "development":
            # Bundle JS/CSS files
            css = Bundle(
                "node_modules/bulma/css/bulma.min.css", filters="cssmin", output="bundle.min.css"
            )

            assets.register("main_css", css)
            css.build()


        return app
