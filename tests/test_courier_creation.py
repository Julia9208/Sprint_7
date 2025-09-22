import pytest
import requests
import allure
from helpers.generator import *
from helpers import Endpoints, COURIER_TEST_DATA

class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_data):
        with allure.step("Создаем курьера"):
            login, password, first_name = courier_data
            payload = {"login": login, "password": password, "firstName": first_name}
            response = requests.post(Endpoints.CREATE_COURIER, json=payload)
        
        with allure.step("Проверяем успешное создание"):
            assert response.status_code == 201, f"Код ответа должен быть 201, получен {response.status_code}"
            assert response.json().get("ok") == True, "Ответ должен содержать ok: true"

    @allure.title("Создание курьера с дублирующимся логином")
    def test_create_duplicate_courier(self, create_and_delete_courier):
        login = create_and_delete_courier[0]
        
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

