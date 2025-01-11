from flask.testing import FlaskClient
from bs4 import BeautifulSoup
from src.models.language_model import LanguageModel


def test_request_translate(app_test: FlaskClient):
    response = app_test.get("/")
    soup = BeautifulSoup(response.text, "html.parser")

    assert (
        soup.find("textarea", {"class": "from-text"}).text
        == "O que deseja traduzir?"
    )
    assert (
        soup.find("textarea", {"class": "to-text"}).text
        == "What do you want to translate?"
    )

    from_languages = [
        language.text
        for language in soup.find(
            "select", {"name": "translate-from"}
        ).find_all("option")
    ]

    assert all(
        language in from_languages
        for language in ["ENGLISH", "AFRIKAANS", "PORTUGUES"]
    )

    to_languages = [
        language.text
        for language in soup.find("select", {"name": "translate-to"}).find_all(
            "option"
        )
    ]

    assert all(
        language in to_languages
        for language in ["ENGLISH", "AFRIKAANS", "PORTUGUES"]
    )

    assert (
        len(from_languages) + len(to_languages)
        == len(LanguageModel.find()) * 2
    )

    selected_from = soup.find("select", {"name": "translate-from"}).find(
        "option", {"selected": True}
    )

    assert selected_from["value"] == "pt"
    assert selected_from.text == "PORTUGUES"

    selected_to = soup.find("select", {"name": "translate-to"}).find(
        "option", {"selected": True}
    )

    assert selected_to["value"] == "en"
    assert selected_to.text == "ENGLISH"


def test_post_translate(app_test: FlaskClient):
    response = app_test.post(
        "/",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )

    soup = BeautifulSoup(response.text, "html.parser")

    assert (
        soup.find("textarea", {"class": "from-text"}).text
        == "Hello, I like videogame"
    )
    assert (
        soup.find("textarea", {"class": "to-text"}).text
        == "Olá, eu gosto de videogame"
    )

    selected_from = soup.find("select", {"name": "translate-from"}).find(
        "option", {"selected": True}
    )

    assert selected_from, "Uma opção 'translate-from' deve estar selecionada"

    assert selected_from["value"] == "en"

    selected_to = soup.find("select", {"name": "translate-to"}).find(
        "option", {"selected": True}
    )

    assert selected_to, "Uma opção 'translate-to' deve estar selecionada"

    assert selected_to["value"] == "pt"


def test_post_reverse(app_test: FlaskClient):
    response = app_test.post(
        "/reverse",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )

    soup = BeautifulSoup(response.text, "html.parser")

    assert (
        soup.find("textarea", {"class": "from-text"}).text
        == "Olá, eu gosto de videogame"
    )
    assert (
        soup.find("textarea", {"class": "to-text"}).text
        == "Hello, I like videogame"
    )

    selected_from = soup.find("select", {"name": "translate-from"}).find(
        "option", {"selected": True}
    )

    assert selected_from, "Uma opção 'translate-from' deve estar selecionada"

    assert selected_from["value"] == "pt"

    selected_to = soup.find("select", {"name": "translate-to"}).find(
        "option", {"selected": True}
    )

    assert selected_to, "Uma opção 'translate-to' deve estar selecionada"

    assert selected_to["value"] == "en"
