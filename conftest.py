from client.client import Client
import requests
from data.constant import BASE_URL
import pytest
from data.constant import SELLER_ID
import faker


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    client = Client(base_url=BASE_URL, session=session)
    yield client
    session.close()


@pytest.fixture()
def announcement_payload(faker_instance):
    return {
        "sellerID": SELLER_ID,
        "name": faker_instance.name(),
        "price": faker_instance.random_int(min=1),
        "statistics": {
            "likes": faker_instance.random_int(min=1),
            "viewCount": faker_instance.random_int(min=1),
            "contacts": faker_instance.random_int(min=1),
        },
    }


@pytest.fixture(scope="session")
def faker_instance() -> faker.Faker:
    return faker.Faker()
