import requests
import pytest


def check_status(expected_status, actual_status):
    assert expected_status == actual_status


def check_response_body(
    response: requests.Response,
    expected_data: dict | None,
    func_check_announcement,
):
    data = response.json()

    if isinstance(data, list):
        for value in data:
            func_check_announcement(value, expected_data)
    elif isinstance(data, dict):
        func_check_announcement(data, expected_data)
    else:
        pytest.fail(f"Неожиданный тип данных: {type(data)}")


def check_base_fields_exist(announcement: dict):
    assert "createdAt" in announcement
    assert "id" in announcement
    assert "sellerId" in announcement
    assert "name" in announcement
    assert "price" in announcement


def check_statistics_fields_exist(data: dict):
    assert "likes" in data
    assert "viewCount" in data
    assert "contacts" in data


def validate_base_fields_values(
    announcement: dict, expected_announcement: dict
):
    assert announcement["id"] == expected_announcement["id"]
    assert announcement["sellerId"] == expected_announcement["sellerID"]
    assert announcement["name"] == expected_announcement["name"]
    assert announcement["price"] == expected_announcement["price"]


def validate_statistics_values(data: dict, expected_data: dict):
    assert data["likes"] == expected_data["likes"]
    assert data["viewCount"] == expected_data["viewCount"]
    assert data["contacts"] == expected_data["contacts"]


def check_required_fields_exist(announcement: dict):
    check_base_fields_exist(announcement)
    check_statistics_fields_exist(announcement["statistics"])


def check_values_announcement(announcement: dict, expected_announcement: dict):
    validate_base_fields_values(announcement, expected_announcement)
    validate_statistics_values(
        announcement["statistics"], expected_announcement["statistics"]
    )


def complex_check_announcement(
    announcement: dict, expected_announcement: dict
):
    check_required_fields_exist(announcement)
    check_values_announcement(announcement, expected_announcement)


def complex_check_statistics(statistics: dict, expected_statistics: dict):
    check_statistics_fields_exist(statistics)
    validate_statistics_values(statistics, expected_statistics)


def check_error_message(response, message: str):
    data = response.json()
    assert data["result"]["message"] == message
