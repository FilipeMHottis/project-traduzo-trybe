from flask import render_template, Blueprint
from models.language_model import LanguageModel


translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def render_languages():
    return render_template(
        "index.html",
        languages=LanguageModel().list_dicts(),
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )
