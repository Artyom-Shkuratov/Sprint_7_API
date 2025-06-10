from Api_Methods.method_api import APIOrder, APICourier
from Data.data import Payloads
import allure

class TestAcceptOrder:
    
    @allure.step('Принятие заказа')
    def test_accept_order(self):
        
        data_couries = Payloads().create_courier_data()
        APICourier.create_courier(data_couries)
        order_response, _ = APIOrder.create_order(Payloads().create_single_order_data())
        track_id = order_response["track"]
        order_info, _ = APIOrder.get_order_by_track(track_id)
        order_id = order_info["order"]["id"]
        courier_response, _ = APICourier.login_courier(data_couries)
        courier_id = courier_response["id"]
        accept_response, status_code = APIOrder.put_order_to_courier(courier_id, order_id)

        assert status_code == 200
        assert accept_response["ok"]
    
    @allure.step('Принятие заказа. Если передать неверный id курьера, то вернется ошибка')
    def test_accept_order_with_wrong_id(self):
        
        order_response,_ = APIOrder.create_order(Payloads().create_single_order_data())
        track_id = order_response['track']
        order_info,_=APIOrder.get_order_by_track(track_id)
        order_id = order_info['order']['id']
        accept_response, accept_status_code = APIOrder.put_order_to_courier('11111',order_id)
        
        assert accept_status_code == 404, f'Вернулся овтет с кодом {accept_status_code}'
        assert accept_response["message"] == "Курьера с таким id не существует"
        
    @allure.title("Принятие заказа. Если не передать  id курьера, запрос вернёт ошибку ")
    def test_accept_order_with_no_courier_id(self):

        order_response, _ = APIOrder.create_order(Payloads().create_single_order_data())
        track = order_response["track"]
        order_info, _ = APIOrder.get_order_by_track(track)
        order_id = order_info["order"]["id"]
        accept_response, status_code = APIOrder.put_order_to_courier("", order_id)

        assert status_code == 400
        assert accept_response["message"] == "Недостаточно данных для поиска"
        
    @allure.title("Принять заказ. Если не передать  номер заказа, то запрос вернёт ошибку ")
    def test_accept_order_with_no_order_id(self):
        
        courier_data = Payloads().create_courier_data()
        APICourier.create_courier(courier_data)
        courier_response, _ = APICourier.login_courier(courier_data)
        courier_id = courier_response["id"]
        accept_response, status_code = APIOrder.put_order_to_courier(courier_id, "")

        assert status_code == 404
        assert accept_response["message"] == "Not Found."



    @allure.title("Принятm заказ. Если передать неверный номер заказа,  вернётся ошибку ")
    def test_accept_order_with_incorrect_order_id(self):

        courier_data = Payloads().create_courier_data()
        APICourier.create_courier(courier_data)
        courier_response, _ = APICourier.login_courier(courier_data)
        courier_id = courier_response["id"]
        accept_response, status_code = APIOrder.put_order_to_courier(courier_id, "9999999")

        assert status_code == 404
        assert accept_response["message"] == "Заказа с таким id не существует"
