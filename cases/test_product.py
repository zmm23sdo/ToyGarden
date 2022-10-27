import os
import sys

from page_admin.product_page import myproduct_page
sys.path.append(os.getcwd())

import pytest
from page_admin import login_page
from faker import Faker

faker = Faker()
params = [("zmwtest","qwer@1234","登录成功！")]

@pytest.fixture(scope="module")
def login(request):
     
    pw = login_page.LoginPage()
    tip = pw.Login(request.param[0], request.param[1])
    assert tip == request.param[2]
    return pw.page   

@pytest.mark.parametrize("login", params, indirect=True )
class TestProduct:

    productname = str(faker.name()*3)
    picname = "./pic.jpeg"
    price = "300"
    stock = "99"
    transPrice = "10"

    def test_createproduct(self, login):
        expect = [(
            self.productname,
            self.picname,
            self.price,
            self.stock,
            self.transPrice
        )
        ]
        for data in expect:
            pw = myproduct_page.ProductPage(login)
            pw.CreateBasicProduct(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]  
            )
        pass















if __name__ == '__main__':
    pytest.main(["cases/test_product.py","-vs"])