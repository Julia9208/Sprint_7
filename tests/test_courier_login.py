import pytest
import requests
from helpers.endpoints import Endpoints

# Класс для тестирования логина курьеров
class TestLoginCourier:
    
    # Тест успешного логина курьера
    def test_login_courier_success(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier
        
        # Данные для логина
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        # Проверяем успешный логин
        assert response.status_code == 200, "Логин должен быть успешным"
        assert "id" in response.json(), "В ответе должен быть ID курьера"
    
    # Тест логина с неправильным паролем
    def test_login_wrong_password(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier
        
        # Пытаемся логиниться с неправильным паролем
        payload = {
            "login": login,
            "password": "wrong_password"
        }
        
        response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        # Должна вернуться ошибка
        assert response.status_code == 404, "Должна быть ошибка 404"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
    
    # Тест логина без логина
    def test_login_missing_login(self):
        payload = {
            "password": "test123"
        }
        
        response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        # Проверяем что вернулась ошибка клиента (4xx)
        assert 400 <= response.status_code < 500, "Должна быть клиентская ошибка"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
    
    # Тест логина без пароля
    def test_login_missing_password(self):
        payload = {
            "login": "testuser"
        }
        
        response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        # Проверяем что вернулась ошибка клиента (4xx)
        assert 400 <= response.status_code < 500, "Должна быть клиентская ошибка"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
    
    # Тест логина несуществующего пользователя
    def test_login_nonexistent_user(self):
        payload = {
            "login": "nonexistent_user",
            "password": "password123"
        }
        
        response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        # Должна вернуться ошибка 404
        assert response.status_code == 404, "Должна быть ошибка 404"
        assert "message" in response.json(), "В ответе должно быть сообщение об ошибке"
        