import pytest
from helpers.help import (
    check_status,
    check_response_body,
    complex_check_announcement,
    check_error_message,
)
import pytest


def test_post_api_1_item(api_client, announcement_payload):
    """Тест падает потому, что ответ колекции не соотвествует реальному ответу см. 1 баг"""
    response = api_client.create_announcement(announcement_payload)
    check_status(200, response.status_code)
    announcement_payload["id"] = response.json()[id]
    check_response_body(
        response, announcement_payload, complex_check_announcement
    )


def test_post_api_1_item_negative_price(
    api_client, announcement_payload
):
    announcement_payload["price"] = -1
    response = api_client.create_announcement(announcement_payload)
    check_status(400, response.status_code)


@pytest.mark.parametrize(
    "field,value,expected_status",
    [
        ("likes", 0, 200),
        ("viewCount", 0, 200),
        ("contacts", 0, 200),
        ("likes", -1, 400),
        ("viewCount", -1, 400),
        ("contacts", -1, 400),
    ],
)
def test_post_api_1_item_with_invalid_code(
    field, value, expected_status, api_client, announcement_payload
):
    announcement_payload["statistics"][field] = value
    response = api_client.create_announcement(announcement_payload)
    check_status(expected_status, response.status_code)


@pytest.mark.parametrize(
    "field,value,message",
    [
        ("sellerID", None, "поле sellerID обязательно"),
        ("name", None, "поле name обязательно"),
        ("price", None, "поле price обязательно"),
        ("likes", None, "поле likes обязательно"),
        ("viewCount", None, "поле viewCount обязательно"),
        ("contacts", None, "поле contacts обязательно"),
        ("sellerID", "str", "поле sellerID должно быть числом"),
        ("name", 123, "поле name должно быть строкой"),
        ("price", "str", "поле price должно быть числом"),
        ("likes", "str", "поле likes должно быть числом"),
        ("viewCount", "str", "поле viewCount должно быть числом"),
        ("contacts", "str", "поле contacts должно быть числом"),
    ],
)
def test_post_api_1_item_with_invalid_values(
    field, value, message, api_client, announcement_payload
):
    announcement_payload[field] = value
    response = api_client.create_announcement(announcement_payload)
    check_status(400, response.status_code)
    check_error_message(response, message)
