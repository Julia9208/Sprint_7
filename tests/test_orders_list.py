import pytest
import requests
import allure
from helpers import Endpoints

class TestOrdersList:

    @allure.title("Получение списка всех заказов")
    def test_get_orders_list(self):
        with allure.step("Запрашиваем список заказов"):
            response = requests.get(Endpoints.GET_ORDERS)
        
        with allure.step("Проверяем успешный ответ"):
            assert response.status_code == 200, "Код должен быть 200"
            assert "orders" in response.json(), "Должен вернуться список заказов"
            assert isinstance(response.json()["orders"], list), "Заказы должны быть списком"

    @allure.title("Получение заказов с лимитом")
    def test_get_orders_with_limit(self):
        with allure.step("Запрашиваем заказы с лимитом 5"):
            response = requests.get(f"{Endpoints.GET_ORDERS}?limit=5")
        
        with allure.step("Проверяем ограничение количества"):
            assert response.status_code == 200, "Код должен быть 200"
            orders = response.json()["orders"]
            assert len(orders) <= 5, "Должно вернуться не более 5 заказов"
            