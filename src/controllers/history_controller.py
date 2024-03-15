from flask import Blueprint
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def index():
    print(HistoryModel.list_as_json())
    return HistoryModel.list_as_json()
