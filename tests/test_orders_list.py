import pytest
import requests
from helpers.endpoints import Endpoints

# Класс для тестирования получения списка заказов
class TestOrdersList:
    
    # Тест получения списка всех заказов
    def test_get_orders_list(self):
        response = requests.get(Endpoints.GET_ORDERS)
        
        # Проверяем успешный ответ
        assert response.status_code == 200, "Запрос должен быть успешным"
        assert "orders" in response.json(), "В ответе должен быть список заказов"
        assert isinstance(response.json()["orders"], list), "Заказы должны быть списком"
    
    # Тест получения заказов с ограничением количества
    def test_get_orders_with_limit(self):
        response = requests.get(f"{Endpoints.GET_ORDERS}?limit=5")
        
        # Проверяем успешный ответ
        assert response.status_code == 200, "Запрос должен быть успешным"
        orders = response.json()["orders"]
        assert len(orders) <= 5, "Должно вернуться не более 5 заказов"
    
    # Тест получения заказов с указанием страницы
    def test_get_orders_with_page(self):
        response = requests.get(f"{Endpoints.GET_ORDERS}?page=0")
        
        # Проверяем успешный ответ
        assert response.status_code == 200, "Запрос должен быть успешным"
        assert "orders" in response.json(), "В ответе должен быть список заказов"
        