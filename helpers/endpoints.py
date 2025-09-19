# Файл с всеми URL-адресами API для удобства использования
class Endpoints:
    # Базовый URL API Яндекс Самокат
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"
    
    # Эндпоинты для работы с курьерами
    CREATE_COURIER = f"{BASE_URL}/courier"          # Создание курьера
    LOGIN_COURIER = f"{BASE_URL}/courier/login"     # Логин курьера
    DELETE_COURIER = f"{BASE_URL}/courier/"         # Удаление курьера (+ id)
    
    # Эндпоинты для работы с заказами
    CREATE_ORDER = f"{BASE_URL}/orders"             # Создание заказа
    GET_ORDERS = f"{BASE_URL}/orders"               # Получение списка заказов
    