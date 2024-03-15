import json
from src.models.history_model import HistoryModel


expected_answer = [
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


# Req. 7
def test_request_history():
    historics = json.loads(HistoryModel.list_as_json())

    for index, historic in enumerate(historics):
        assert (
            historic["text_to_translate"]
            == expected_answer[index]["text_to_translate"]
        )
        assert (
            historic["translate_from"]
            == expected_answer[index]["translate_from"]
        )
        assert (
            historic["translate_to"] == expected_answer[index]["translate_to"]
        )
