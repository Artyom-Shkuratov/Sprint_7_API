from Api_Methods.method_api import APICourier
from Data.data import Payloads
from Data.urls import Urls
import pytest
import allure


class TestCourierRegister:

    @allure.title("Проверяем, что курьера можно создать")
    def test_create_courier(self):
        data = Payloads().create_courier_data()
        response = APICourier.create_courier(data)
        assert response["ok"], "Учетная запись курьера не создалась"

    @allure.title("Проверяем, что нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        data = Payloads().create_courier_data()
        APICourier.create_courier(data)
        response = APICourier.create_courier(data)
        assert response["message"] == "Этот логин уже используется. Попробуйте другой.", "Курьер с одинаковыми данным не должен создаваться"

    @allure.title("Проверяем, что нельзя создать курьера без обязательных полей (логина и пароля)")
    @pytest.mark.parametrize("data", Payloads.get_create_courier_invalid_payloads())
    def test_create_courier_with_missing_fields(self, data):
        response = APICourier.create_courier(data)
        assert response["code"] == 400, "Курьер не должен создаваться без логина или без пароля" 