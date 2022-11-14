from flask import Blueprint, jsonify

action = Blueprint("action", __name__)

@action.route("/actions")
def actions():
    return jsonify(["on", "off"])

@action.route("/action/on")
def on():
    return jsonify({"on": True})
