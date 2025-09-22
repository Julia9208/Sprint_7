# Тестовые данные (вынесено из тестов)
COURIER_TEST_DATA = {
    "missing_login": {"password": "test123", "firstName": "Test"},
    "missing_password": {"login": "testuser", "firstName": "Test"},
    "missing_first_name": {"login": "testuser", "password": "test123"},
    "nonexistent_user": {"login": "nonexistent_user", "password": "password123"}
}

ORDER_TEST_DATA = {
    "basic_order": {
        "firstName": "Иван",
        "lastName": "Иванов", 
        "address": "ул. Пушкина, д. 10",
        "metroStation": "4",
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2024-12-31",
        "comment": "Тестовый заказ"
    },
    "minimal_order": {
        "firstName": "Петр",
        "lastName": "Петров",
        "address": "ул. Лермонтова, д. 5",
        "metroStation": "2",
        "phone": "+79997654321",
        "rentTime": 2,
        "deliveryDate": "2024-11-30",
        "comment": "Второй тестовый заказ"
    }
}
