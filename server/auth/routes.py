from flask import Blueprint, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import os

auth_blueprint = Blueprint("auth", __name__)

google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_OAUTH_CLIENT_SECRET"),
    scope=["profile", "email"]
)

auth_blueprint.register_blueprint(google_bp, url_prefix="/login")

@auth_blueprint.route("/google")
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    return resp.json()