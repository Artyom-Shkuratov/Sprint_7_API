from Api_Methods.method_api import APIOrder, APICourier
from Data.data import Payloads
import allure
import json


@allure.feature("Список заказов")
class TestGetOrderList:
    
    @allure.title("Получаем список заказов по id")
    def test_get_order_by_id(self):
        #Создаем курьера
        data = Payloads().create_courier_data()
        APICourier.create_courier(data)
        #Логинимся курьером
        login_response, _ = APICourier.login_courier(data)
        id_couriers = login_response['id']
        #Создаем заказ
        user_order = json.dumps(Payloads().create_single_order_data())
        response_order, _ = APIOrder.create_order(user_order)
        track_id = response_order['track']
        # получаем ID заказа по track
        order_info, _ = APIOrder.get_order_by_track(track_id)
        responce_order_id = order_info['order']['id']
        # принимаем заказ курьером
        APIOrder.put_order_to_courier(id_couriers,responce_order_id)
        #запрашиваем список заказов
        response_order, status_code_order = APIOrder.get_orders_list()
        
        assert response_order, "Ответ не вернул список заказов"
        assert status_code_order == 200, " Статус код должен быть = 200"
        
    
        
        
        
        
        
