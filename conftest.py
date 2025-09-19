import pytest
import requests
import random
import string
from helpers.endpoints import Endpoints

# Функция для генерации случайных строк (для создания уникальных тестовых данных)
def generate_random_string(length=10):
    letters = string.ascii_lowercase  # Все буквы в нижнем регистре
    return ''.join(random.choice(letters) for i in range(length))

# Фикстура для создания и удаления тестового курьера
@pytest.fixture
def create_and_delete_courier():
    # Генерируем уникальные данные для курьера
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()
    
    # Создаем тело запроса для регистрации курьера
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    # Отправляем POST-запрос для создания курьера
    response = requests.post(Endpoints.CREATE_COURIER, json=payload)
    
    # Если курьер создан успешно, логинимся чтобы получить его ID
    courier_id = None
    if response.status_code == 201:
        login_payload = {"login": login, "password": password}
        login_response = requests.post(Endpoints.LOGIN_COURIER, json=login_payload)
        
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
    
    # Возвращаем данные курьера тесту
    yield login, password, courier_id
    
    # После выполнения теста удаляем курьера
    if courier_id:
        requests.delete(f"{Endpoints.DELETE_COURIER}{courier_id}")
        