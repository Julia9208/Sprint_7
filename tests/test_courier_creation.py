import pytest
import requests
from helpers.endpoints import Endpoints

# Класс для тестирования создания курьеров
class TestCreateCourier:
    
    # Тест успешного создания курьера
    def test_create_courier_success(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier
        
        # Проверяем что все данные получены (значит курьер создан)
        assert login is not None, "Логин не должен быть пустым"
        assert password is not None, "Пароль не должен быть пустым"
        assert courier_id is not None, "ID курьера не должен быть пустым"
    
    # Тест создания курьера с дублирующимся логином
    def test_create_duplicate_courier(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier
        
        # Пытаемся создать второго курьера с таким же логином
        payload = {
            "login": login,
            "password": "different_password",
            "firstName": "different_name"
        }
        
        response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        # Должна вернуться ошибка конфликта (409)
        assert response.status_code == 409, "Должна быть ошибка конфликта"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
    
    # Тест создания курьера без логина
    def test_create_courier_missing_login(self):
        payload = {
            "password": "test123",
            "firstName": "Test"
        }
        
        response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        # Проверяем что вернулась ошибка клиента (4xx)
        assert 400 <= response.status_code < 500, "Должна быть клиентская ошибка"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
    
    # Тест создания курьера без пароля
    def test_create_courier_missing_password(self):
        payload = {
            "login": "testuser",
            "firstName": "Test"
        }
        
        response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        # Проверяем что вернулась ошибка клиента (4xx)
        assert 400 <= response.status_code < 500, "Должна быть клиентская ошибка"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
    
    # Тест создания курьера без имени
    def test_create_courier_missing_first_name(self):
        payload = {
            "login": "testuser",
            "password": "test123"
        }
        
        response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        # Проверяем что вернулась ошибка клиента (4xx)
        assert 400 <= response.status_code < 500, "Должна быть клиентская ошибка"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
        