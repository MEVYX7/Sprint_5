import random

class Generators:
    def generate_email():
        return f"test_user_{random.randint(100,999)}@yandex.ru"

    def generate_password():
        return f"pass{random.randint(100000,999999)}"