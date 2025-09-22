import random
import string

# Функция для генерации случайных строк (вынесено из conftest.py)
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

