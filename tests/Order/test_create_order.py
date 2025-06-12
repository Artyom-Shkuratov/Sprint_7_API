from Api_Methods.method_api import APIOrder
from Data.data import Payloads
import pytest
import json
import allure


@allure.feature("Создание заказа")
class TestCreateOrder:
    
    @allure.title('Проверяем, что при создании заказа можно указать: один цвет, оба цвета или без цвета. Ответ должен содержать track_ID')
    @pytest.mark.parametrize("order", Payloads().create_multiple_order_data())
    def test_create_order(self, order):
        user_order = json.dumps(order)
        responce,status_code = APIOrder.create_order(user_order)
        
        assert status_code == 201, f'Статус кода не правильный, вернулся {status_code}'
        assert responce['track'], 'ID не получен'
        