from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
from .conftest import app_test
from unittest.mock import patch

# file authorship: thiago guarino

# Mock paths
USER_FIND_PATH = "src.models.user_model.AbstractModel.find_one"
TOKEN_VALIDATION_PATH = "src.models.user_model.UserModel.token_is_valid"
HISTORY_FIND_PATH = "src.models.history_model.HistoryModel.find_one"
HISTORY_DELETE_PATH = "src.models.history_model.AbstractModel.delete"


# Task 9
@patch(USER_FIND_PATH)
@patch(TOKEN_VALIDATION_PATH)
@patch(HISTORY_FIND_PATH)
@patch(HISTORY_DELETE_PATH)
def test_history_delete_unauthorized(
    mock_history_delete,
    mock_history_find,
    mock_token_validation,
    mock_user_find,
    app_test: app_test
):

    mock_user_data = {"name": "User Test", "token": "token_test"}
    user = UserModel(data=mock_user_data)
    mock_history_data = {
        "_id": "id_test",
        "text_to_translate": "Test text",
        "translate_from": "en",
        "translate_to": "pt"
    }
    history = HistoryModel(json_data=mock_history_data)
    history_id = mock_history_data["_id"]

    mock_user_find.return_value = user
    mock_token_validation.return_value = True
    mock_history_find.return_value = history
    mock_history_delete.return_value = True

    # Act
    response = app_test.delete(
        f"/admin/history/{history_id}",
        headers={
            "Authorization": user.data["token"],
            "User": user.data["name"]
        }
    )

    # Assert
    assert response.status_code == 500
