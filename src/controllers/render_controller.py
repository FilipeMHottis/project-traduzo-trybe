from flask import Blueprint, render_template
from models.language_model import LanguageModel


render_controller = Blueprint("render_controller", __name__)


@render_controller.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )
