import pytest
import requests
from helpers.endpoints import Endpoints

# Класс для тестирования создания заказов
class TestCreateOrder:
    
    # Параметризованный тест создания заказов с разными цветами
    @pytest.mark.parametrize("color", [
        ["BLACK"],      # Только черный цвет
        ["GREY"],       # Только серый цвет
        ["BLACK", "GREY"],  # Оба цвета
        []              # Без цвета
    ])
    def test_create_order_with_different_colors(self, color):
        # Данные для создания заказа
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "ул. Пушкина, д. 10",
            "metroStation": "4",
            "phone": "+79991234567",
            "rentTime": 3,
            "deliveryDate": "2024-12-31",
            "comment": "Тестовый заказ"
        }
        
        # Добавляем цвет если он указан
        if color:
            payload["color"] = color
        
        # Создаем заказ
        response = requests.post(Endpoints.CREATE_ORDER, json=payload)
        
        # Проверяем успешное создание заказа
        assert response.status_code == 201, "Заказ должен быть создан успешно"
        assert "track" in response.json(), "В ответе должен быть трек-номер"
        assert isinstance(response.json()["track"], int), "Трек-номер должен быть числом"
    
    # Тест создания заказа без указания цвета
    def test_create_order_without_color(self):
        payload = {
            "firstName": "Петр",
            "lastName": "Петров",
            "address": "ул. Лермонтова, д. 5",
            "metroStation": "2",
            "phone": "+79997654321",
            "rentTime": 2,
            "deliveryDate": "2024-11-30",
            "comment": "Второй тестовый заказ"
        }
        
        response = requests.post(Endpoints.CREATE_ORDER, json=payload)
        
        # Проверяем успешное создание заказа
        assert response.status_code == 201, "Заказ должен быть создан успешно"
        assert "track" in response.json(), "В ответе должен быть трек-номер"
        