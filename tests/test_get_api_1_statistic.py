from helpers.help import (
    complex_check_statistics,
    check_status,
    check_response_body,
)


def test_get_api_1_statistic(api_client, announcement_payload):
    response = api_client.create_announcement(announcement_payload)
    status_text = response.json()["status"]
    id = status_text.split(" - ")[-1]
    response = api_client.get_statistic(id)
    check_status(200, response.status_code)
    announcement_payload["id"] = id
    check_response_body(
        response, announcement_payload["statistics"], complex_check_statistics
    )


def test_get_api_1_statistic_with_invalid_id(api_client):
    response = api_client.get_announcement("-1")
    check_status(400, response.status_code)
