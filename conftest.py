import pytest
from Api_Methods.method_api import APICourier
from Data.data import Payloads

@pytest.fixture
def created_courier():
    data = Payloads().create_courier_data()
    APICourier.create_courier(data)
    yield data  
    login_response, _ = APICourier.login_courier(data)
    APICourier.delete_courier(login_response["id"])


@pytest.fixture
def create_data_couriers():
    return Payloads().create_courier_data()
    

@pytest.fixture
def created_courier_without_delete():
    data = Payloads().create_courier_data()
    APICourier.create_courier(data)
    return data  
