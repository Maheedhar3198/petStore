import requests
from test_api import BASE_URL

def test_patch_user():
    payload = {
        "name": "Maheedhar",
        "job": "Senior QA Engineer"  # only updating job
    }
    response = requests.patch(f"{BASE_URL}/users/2", json=payload)

    print(response.status_code)
    print(response.json())
    assert response.status_code == 200