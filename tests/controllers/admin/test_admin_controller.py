from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
from src.app import app
import pytest
from bson.objectid import ObjectId


history_test = {
    "text_to_translate": "test",
    "translate_from": "pt",
    "translate_to": "en",
}

user_test = {
    "name": "test_name",
    "level": "admin",
    "token": "test_token",
}


@pytest.fixture(scope="function")
def client():
    app.testing = True
    app_test = app.test_client()
    yield app_test

    HistoryModel.drop()
    UserModel.drop()


@pytest.fixture(scope="function")
def user():
    user = UserModel(user_test)
    user.save()
    yield user
    user.drop()


@pytest.fixture(scope="function")
def history():
    history = HistoryModel(history_test)
    history.save()
    yield history
    history.drop()


@pytest.fixture(scope="function")
def object_id():
    return ObjectId()


def test_history_delete(client, user, history):
    response = client.delete(
        f"/admin/history/{history.id}",
        headers={
            "Authorization": user.data["token"],
            "User": user.data["name"],
        },
    )

    assert response.status_code == 204


def test_unauthorized_access(client, user, history):
    response = client.delete(
        f"/admin/history/{history.id}",
        headers={
            "Authorization": "invalid_token",
            "User": user.data["name"],
        },
    )

    assert response.status_code == 401
    assert response.json == {"error": "Unauthorized Access"}


def test_history_not_found(client, user, object_id):
    response = client.delete(
        f"/admin/history/{object_id}",
        headers={
            "Authorization": user.data["token"],
            "User": user.data["name"],
        },
    )

    assert response.status_code == 404
    assert response.json == {"error": "History not found"}
