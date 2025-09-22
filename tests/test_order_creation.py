import pytest
import requests
import allure
from helpers import Endpoints, ORDER_TEST_DATA

class TestCreateOrder:

    @pytest.mark.parametrize("color, color_name", [
        (["BLACK"], "черный"),
        (["GREY"], "серый"),
        (["BLACK", "GREY"], "оба цвета")
    ])
    @allure.title("Создание заказа с цветом: {color_name}")
    def test_create_order_with_colors(self, color, color_name):
        with allure.step("Подготавливаем данные заказа"):
            payload = ORDER_TEST_DATA["basic_order"].copy()
            payload["color"] = color
        
        with allure.step("Создаем заказ"):
            response = requests.post(Endpoints.CREATE_ORDER, json=payload)
        
        with allure.step("Проверяем успешное создание"):
            assert response.status_code == 201, "Код должен быть 201"
            assert "track" in response.json(), "Должен вернуться track номер"
            assert isinstance(response.json()["track"], int), "Track должен быть числом"

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        with allure.step("Создаем заказ без цвета"):
            payload = ORDER_TEST_DATA["basic_order"]
            response = requests.post(Endpoints.CREATE_ORDER, json=payload)
        
        with allure.step("Проверяем успешное создание"):
            assert response.status_code == 201, "Код должен быть 201"
            assert "track" in response.json(), "Должен вернуться track номер"
            