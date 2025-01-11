import json
from src.models.history_model import HistoryModel

# file authorship: thiago guarino


# Task 7
def test_request_history():
    expected_history_logs = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]

    history_logs = json.loads(HistoryModel.list_as_json())

    for history in history_logs:
        history.pop('_id', None)

    assert expected_history_logs == history_logs
