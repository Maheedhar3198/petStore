from TestData import env
import pytest


@pytest.fixture(scope='session')
def credentials():
    return {"username": env.USERNAME, "password": env.PASSWORD}


@pytest.fixture(scope='session')
def base_url():
    return env.BASE_URL


