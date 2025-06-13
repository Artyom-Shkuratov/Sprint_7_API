from faker import Faker
import allure
import json

faker = Faker()

class Payloads:

    @allure.step("Создание данных курьера")
    def create_courier_data(self):
        data = {"login": faker.name(), "password": str(faker.pyint()), "firstName": faker.first_name()}
        return data
    
    
    @allure.step("Создание одного заказа")
    def create_single_order_data(self):

        data = {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": faker.phone_number(),
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
                }
        return json.dumps(data)
    
    
    @staticmethod
    @allure.step("Создание неполных данных при создании курьера")
    def get_create_courier_invalid_payloads():
        return [
            {"login": faker.name(), "firstName": faker.first_name()},
            {"password": str(faker.pyint()), "firstName": faker.first_name()},
            {"login": faker.name()},
            {"password": str(faker.pyint())},
            {"firstName": faker.first_name()},
        ]
        
    @allure.step("Создание данных заказа")
    def create_multiple_order_data(self):

        data = [
            {
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": faker.phone_number(),
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha",
                "color": ["BLACK"],
            },
            {
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": faker.phone_number(),
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha",
                "color": ["GREY"],
            },
            {
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": faker.phone_number(),
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha",
                "color": ["BLACK", "GREY"],
            },
            {
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "address": "Osaka, 537-0022 apt.",
                "metroStation": 4,
                "phone": faker.phone_number(),
                "rentTime": 5,
                "deliveryDate": "2025-06-15",
                "comment": "Saske, come back to Konoha",
            },
        ]
        
        return data

    @allure.step("Создаем рандомный номер заказа")
    def generate_random_track_order_id(self):
        track_id = faker.pyint(min_value=100000, max_value=999999)
        return track_id