from Api_Methods.method_api import APIOrder, APICourier
from Data.data import Payloads
import allure


class TestGetOrderById:

    @allure.step('Получаем заказ по его номеру')
    def test_get_order_with_correct_track_id(self):
        response, _ = APIOrder.create_order(Payloads().create_single_order_data())
        order_track = response['track']
        info_order,status_code_order = APIOrder.get_order_by_track(order_track)
        
        assert status_code_order == 200, 'КОд ответа должен быть 200'
        assert info_order['order']
        
        
        
    @allure.step('Получаем ошибку при попытке получит заказ без номера')
    def test_get_order_without_track_id(self):
        response,status_code = APIOrder.get_order_by_track('')
        
        assert status_code == 400, f'Код ответа должен быть 400, а вернулся {status_code}'
        assert response['message'] == "Недостаточно данных для поиска"
        
    @allure.step('Получаем ошибку при попытке получит заказ по несуществующему номера')
    def test_get_order_whith_wrong_track_id(self):
        response,status_code = APIOrder.get_order_by_track(Payloads().generate_random_track_order_id())
        
        assert status_code == 404, f'Вернулся код {status_code} '
        assert response['message'] == "Заказ не найден"