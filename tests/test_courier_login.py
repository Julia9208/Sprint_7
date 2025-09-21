import pytest
import requests
import allure
from helpers import Endpoints, COURIER_TEST_DATA

class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier
        
        with allure.step("Выполняем логин"):
            payload = {"login": login, "password": password}
            response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        with allure.step("Проверяем успешный логин"):
            assert response.status_code == 200, "Код должен быть 200"
            assert "id" in response.json(), "Должен вернуться ID курьера"

    @allure.title("Логин с неправильным паролем")
    def test_login_wrong_password(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier
        
        with allure.step("Пытаемся логиниться с неправильным паролем"):
            payload = {"login": login, "password": "wrong_password"}
            response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        with allure.step("Проверяем ошибку"):
            assert response.status_code == 404, "Должна быть ошибка 404"
            assert "message" in response.json(), "Должно быть сообщение об ошибке"

    @pytest.mark.parametrize("test_data", [
        ("missing_login", 400),
        ("missing_password", 400),
        ("nonexistent_user", 404)
    ])
    @allure.title("Логин с проблемными данными: {test_data[0]}")
    def test_login_problem_cases(self, test_data):
        field_name, expected_code = test_data
        
        with allure.step("Отправляем запрос с проблемными данными"):
            payload = COURIER_TEST_DATA[field_name]
            response = requests.post(Endpoints.LOGIN_COURIER, json=payload)
        
        with allure.step("Проверяем ответ"):
            assert response.status_code == expected_code, f"Код должен быть {expected_code}"
            if expected_code != 504:  # Пропускаем проверку для таймаута
                assert "message" in response.json(), "Должно быть сообщение об ошибке"
                