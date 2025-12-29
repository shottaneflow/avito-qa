from helpers.help import check_status


def test_get_api_1_seller_id_item(api_client):
    response = api_client.seller_announcements("111111")
    check_status(200, response.status_code)


def test_get_api_1_seller_id_item_with_invalid_id(api_client):
    response = api_client.get_announcement("-1")
    check_status(400, response.status_code)
