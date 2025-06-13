import pytest
from Api_Methods.method_api import APICourier
from Data.data import Payloads

@pytest.fixture
def create_courier():
    data = Payloads().create_courier_data()
    APICourier.create_courier(data)
    yield data
    login_response, _ = APICourier.login_courier(data)
    if "id" in login_response:
        APICourier.delete_courier(login_response["id"])




@pytest.fixture
def created_courier_without_delete():
    data = Payloads().create_courier_data()
    APICourier.create_courier(data)
    return data  
