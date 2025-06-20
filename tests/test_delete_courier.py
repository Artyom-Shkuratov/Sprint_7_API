from Api_Methods.method_api import APICourier
from Data.data import Payloads
from Data.urls import Urls
import pytest
import allure


class TestDeleteCourier:
    
    @allure.step('Создаем и удаляем курьера')
    def test_delete_courier(self,created_courier_without_delete):
        
       APICourier.create_courier(created_courier_without_delete)
       responce,_ = APICourier.login_courier(created_courier_without_delete)
       id_couriers = responce['id']
       d_responce, d_satus_code = APICourier.delete_courier(id_couriers)
       
       assert d_responce['ok'], 'Курьер не удален'
       assert d_satus_code == 200
       
       
    @allure.title("Отправка запроса с несуществующим ID")
    def test_delete_courier_without_id(self):
        del_response, del_status_code = APICourier.delete_courier("1233455")
        
        assert del_status_code == 404, "Код ответа должен быть 404"
        assert del_response["message"] == 'Курьера с таким id ненайден.'
        
        
    @allure.title("Создаем и потом удаляем курьера без ID")
    def test_delete_courier_without_id(self, created_courier_without_delete):
        APICourier.create_courier(created_courier_without_delete)
        _, _ = APICourier.login_courier(created_courier_without_delete)
        del_response, del_status_code = APICourier.delete_courier("")

        assert del_status_code == 404, "Код ответа должен быть 404"
        assert del_response["message"] == "Not Found.", "Учетная запись курьера не должна была удалена"
