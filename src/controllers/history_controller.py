from flask import Blueprint, jsonify
from models.history_model import HistoryModel

# file authorship: thiago guarino


# task 8
history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history():
    history_log = HistoryModel.list_as_json()
    return jsonify(history_log), 200
