import pytest
import env

@pytest.fixture(scope='session')     #from the error4
def credentials():
    return {"username": env.USERNAME, "password": env.PASSWORD}

@pytest.fixture(scope='session')
def base_url():
    return env.BASE_URL

