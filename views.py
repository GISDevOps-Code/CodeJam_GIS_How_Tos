from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html", name="Tim")

@views.route("/profile")
def profile(username):
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

@views.route("/json")
def get_json():
    return jsonify({'name': 'Tim', 'coolness': 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))

@views.route("/profile_html")
def profile_html():
    return render_template("profile.html")

@views.route("/examples")
def examples():
    return render_template("Examples.html")

@views.route("/python")
def python():
    return render_template("python.html")

@views.route("/colorbrewer")
def colorbrewer():
    return render_template("colorbrewer.html")

@views.route("/topology")
def topology():
    return render_template("topology.html")

@views.route("/cartography")
def cartography():
    return render_template("cartography.html")

@views.route("/fish")
def fish():
    return render_template("fish.html")

@views.route("/drawings")
def drawings():
    return render_template("drawings.html")