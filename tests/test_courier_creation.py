import pytest
import requests
import allure
import random
import string
from helpers import Endpoints, COURIER_TEST_DATA

class TestCreateCourier:

    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        with allure.step("Генерируем данные курьера"):
            login = "test_user_" + self.generate_random_string(8)
            password = "password123"
            first_name = "Test User"
        
        with allure.step("Создаем курьера"):
            payload = {"login": login, "password": password, "firstName": first_name}
            response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        with allure.step("Проверяем успешное создание"):
            assert response.status_code == 201, f"Код ответа должен быть 201, получен {response.status_code}"
            assert response.json().get("ok") == True, "Ответ должен содержать ok: true"
        
        with allure.step("Удаляем тестового курьера"):
            login_response = requests.post(Endpoints.LOGIN_COURIER, 
                                         json={"login": login, "password": password})
            if login_response.status_code == 200:
                courier_id = login_response.json().get("id")
                requests.delete(f"{Endpoints.DELETE_COURIER}{courier_id}")

    @allure.title("Создание курьера с дублирующимся логином")
    def test_create_duplicate_courier(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier
        
        with allure.step("Пытаемся создать дубликат курьера"):
            payload = {
                "login": login,
                "password": "different_password",
                "firstName": "different_name"
            }
            response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        with allure.step("Проверяем ошибку конфликта"):
            assert response.status_code == 409, f"Должна быть ошибка 409, получен {response.status_code}"
            assert "message" in response.json(), "Должно быть сообщение об ошибке"

    @pytest.mark.parametrize("field_name, expected_codes", [
        ("missing_login", [400, 409]),
        ("missing_password", [400, 409]),
        ("missing_first_name", [400, 409])
    ])
    @allure.title("Создание курьера без обязательных полей: {field_name}")
    def test_create_courier_missing_fields(self, field_name, expected_codes):
        with allure.step(f"Отправляем запрос без поля {field_name}"):
            payload = COURIER_TEST_DATA[field_name]
            response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        with allure.step("Проверяем ошибку клиента"):
            assert response.status_code in expected_codes, f"Код должен быть одним из {expected_codes}, получен {response.status_code}"
            assert "message" in response.json(), "Должно быть сообщение об ошибке"
            
