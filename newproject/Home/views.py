from flask import (Blueprint, render_template, redirect, url_for)

home_blueprint = Blueprint("Home", __name__, template_folder="templates/Home")


@home_blueprint.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')