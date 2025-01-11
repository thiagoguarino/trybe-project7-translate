from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel

# file authorship: thiago guarino

translate_controller = Blueprint("translate_controller", __name__)


# Tasks 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        languages = LanguageModel.list_dicts()

        translate_from = "pt"
        translate_to = "en"

        text_to_translate = "O que deseja traduzir?"
        translated = "What do you want to translate?"

        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated
        )

    if request.method == "POST":
        languages = LanguageModel.list_dicts()

        translate_from = request.form["translate-from"]
        translate_to = request.form["translate-to"]

        text_to_translate = request.form["text-to-translate"]
        translated = GoogleTranslator(
            source=translate_from,
            target=translate_to
        ).translate(text_to_translate)

        data = {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }

        HistoryModel(json_data=data).save()

        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated
        )


# Tasks 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()

    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    text_to_translate = request.form.get("text-to-translate")
    translated = GoogleTranslator(
        source=translate_from,
        target=translate_to
    ).translate(text_to_translate)

    data = {
            "text_to_translate": text_to_translate,
            "translate_from": translate_to,
            "translate_to": translate_from,
    }

    HistoryModel(json_data=data).save()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated,
        translated=text_to_translate,
        translate_from=translate_to,
        translate_to=translate_from
    )
