import requests
import pytest
import env

@pytest.mark.parametrize("post_id",[1,2,3,4,5,6])
def test_get_users(post_id):
    response = requests.get(f"{env.url()}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["id"] == post_id
    assert isinstance(data["userId"],int),f"userId is not an integer"
    assert isinstance(data["title"], str),f"title is not a string"
    assert isinstance(data["body"], str),f"body is not a string"

@pytest.mark.parametrize("title_name",["Nani","Surya","Rahul","Chandra"])
def test_create_user(title_name):
    payload = {
        "userId": 1,
        "title": f"{title_name}",
        "body": "This is a test post manually created via Postman."
    }
    response = requests.post(f"{env.url()}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == f"{title_name}"


