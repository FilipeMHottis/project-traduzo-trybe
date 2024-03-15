from flask import Blueprint, render_template, request
from typing import TypedDict
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator


render_controller = Blueprint("render_controller", __name__)


class FormRequest(TypedDict):
    text_to_translate: str
    translate_from: str
    translate_to: str


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


@render_controller.route("/", methods=["POST"])
def translate():
    data: FormRequest = {
        "text_to_translate": request.form.get("text-to-translate"),
        "translate_from": request.form.get("translate-from"),
        "translate_to": request.form.get("translate-to"),
    }
    translated = GoogleTranslator(
        source=data["translate_from"], target=data["translate_to"]
    ).translate(data["text_to_translate"])

    print(data["translate_from"])

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=data["text_to_translate"],
        translate_from=data["translate_from"],
        translate_to=data["translate_to"],
        translated=translated,
    )
