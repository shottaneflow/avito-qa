import requests


class Client:

    def __init__(self, base_url: str, session: requests.Session) -> None:
        self.base_url = base_url
        self.session = session

    def create_announcement(self, data: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/api/1/item", json=data)

    def get_announcement(self, id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/1/item/{id}")

    def get_statistic(self, id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/1/statistic/{id}")

    def seller_announcements(self, seller_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/1/{seller_id}/item")
