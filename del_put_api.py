import requests
import pytest
import env


@pytest.mark.parametrize("title_name", ["Nani", "Surya", "Rahul", "Chandra"])
def test_patch(title_name):
    payload = {
        "userId": 1,
        "title": f"{title_name}",
        "body": "This is a test post manually updated via Postman."
    }
    response = requests.patch(env.url(), json=payload, headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == f"{title_name}"


@pytest.mark.parametrize("title_name", ["Nani", "Surya", "Rahul", "Chandra"])
def test_put(title_name):
    payload = {
        "userId": 1,
        "title": f"{title_name}"
    }
    response = requests.put(env.url(), json=payload, headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == f"{title_name}"
    print(f"PUT Response for title {title_name}: {data}")


@pytest.mark.parametrize("post_id", [1, 2, 3, 4])
def test_delete(post_id):
    response = requests.delete(env.url() + str(post_id))
    assert response.status_code == 200
    data = response.json()
    assert data == {}

@pytest.mark.parametrize("post_id", [999, "invalid", -1])
def test_delete_negative(post_id):
    response = requests.delete(env.url() + str(post_id))
    assert response.status_code != 200
    data = response.json()
    assert data != {}





