from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
from bson.objectid import ObjectId
import json


def history():
    HistoryModel(
        {
            "text_to_translate": "test",
            "translate_from": "pt",
            "translate_to": "en",
        }
    ).save()

    return HistoryModel.find_one({"text_to_translate": "test"}).data["_id"]


def user():
    UserModel(
        {"name": "test_name", "level": "admin", "token": "test_token"}
    ).save()

    return {"name": "test_name", "level": "admin", "token": "test_token"}


def test_history_delete(app_test):
    user_test = user()
    history_id = history()

    response = app_test.delete(
        f"/admin/history/{history_id}",
        headers={
            "Authorization": user_test["token"],
            "User": user_test["name"],
        },
    )

    assert response.status_code == 204


def test_history_delete_unauthorized(app_test):
    history_id = history()

    response = app_test.delete(
        f"/admin/history/{history_id}",
        headers={
            "Authorization": "invalid_token",
            "User": "invalid_user",
        },
    )

    assert response.status_code == 401
    assert json.loads(response.data) == {"error": "Unauthorized Access"}


def test_history_not_found(app_test):
    user_test = user()

    response = app_test.delete(
        f"/admin/history/{ObjectId()}",
        headers={
            "Authorization": user_test["token"],
            "User": user_test["name"],
        },
    )

    assert response.status_code == 404
    assert json.loads(response.data) == {"error": "History not found"}
