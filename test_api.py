import requests

BASE_URL = "https://reqres.in/api"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

def test_create_user():
    payload = {
        "name": "Maheedhar",
        "job": "QA Automation Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Maheedhar"
