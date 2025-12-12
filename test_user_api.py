import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_by_id():
    session = requests.Session()
    response = session.get(f"{BASE_URL}/users/{1}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()
    structure_validation_user(response_json)

    assert response_json["id"] == 1
    assert response_json["name"] == "Leanne Graham"
    assert response_json["username"] == "Bret"
    assert response_json["email"] == "Sincere@april.biz"
    assert "770-736-8031" in response_json["phone"]

def test_create_user():
    session = requests.Session()
    user_data = {
        "name": "Aleksei Petrov",
        "username": "aleksei_qa",
        "email": "aleksei.petrov@example.com",
        "phone": "1-234-567-8900",
        "website": "aleksei-qa.dev"
    }
    response = session.post(f"{BASE_URL}/users", json=user_data)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    response_json = response.json()
    structure_validation_user(response_json)

    assert response_json["name"] == user_data["name"]
    assert response_json["username"] == user_data["username"]
    assert response_json["email"] == user_data["email"]
    assert response_json["phone"] == user_data["phone"]
    assert response_json["website"] == user_data["website"]

def test_update_user():
    session = requests.Session()
    update_data = {
        "name": "Leanne Graham Updated",
        "username": "Bret_Updated",
        "email": "leanne.updated@example.com",
        "phone": "1-770-736-8031 x99999",
        "website": "leanne-updated.org"
    }
    response = session.put(f"{BASE_URL}/users/1", json=update_data)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()
    structure_validation_user(response_json)

    assert response_json["name"] == update_data["name"]
    assert response_json["username"] == update_data["username"]
    assert response_json["email"] == update_data["email"]
    assert response_json["phone"] == update_data["phone"]
    assert response_json["website"] == update_data["website"]

def structure_validation_user(response_json):
    assert "id" in response_json
    assert "name" in response_json
    assert "username" in response_json
    assert "email" in response_json
    assert "phone" in response_json

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
