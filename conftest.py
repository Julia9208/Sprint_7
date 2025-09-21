import pytest
import requests
from helpers import Endpoints, generate_random_string

@pytest.fixture
def create_and_delete_courier():
    # Генерируем уникальные данные для курьера
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # Создаем курьера
    response = requests.post(Endpoints.CREATE_COURIER, json=payload)
    
    courier_id = None
    if response.status_code == 201:
        login_payload = {"login": login, "password": password}
        login_response = requests.post(Endpoints.LOGIN_COURIER, json=login_payload)
        
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")

    yield login, password, courier_id

    if courier_id:
        requests.delete(f"{Endpoints.DELETE_COURIER}{courier_id}")
