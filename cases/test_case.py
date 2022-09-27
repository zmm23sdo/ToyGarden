import os
import sys
sys.path.append(os.getcwd())

import pytest
from page_admin import login_page, product_page
from faker import Faker
import datetime
import json

params = [("admin","qwer@1234","登录成功！")]

# @pytest.mark.dependency()
@pytest.fixture(scope="module")
def login(request):
     
    pw = login_page.LoginPage()
    tip = pw.login(request.param[0], request.param[1])
    assert tip == request.param[2]
    return pw.page   

class TestCase:

    @pytest.mark.dependency()
    def test_login(self):
        pw = login_page.LoginPage()
        expect = [
            {
                "username":"qwer@1234",
                "password":"admin",
                "bubble":"登录失败，请重试！"
            },
            {
                "username":"admin",
                "password":"qwer@1234",
                "bubble":"登录成功！"
            }
        ]
        for data in expect:
            tip = pw.login(
                data["username"],
                data["password"]
            )
            assert tip == data["bubble"]


    productname = str(Faker().name()*3)
    picname = "./pic.jpeg"
    price = "300"
    stock = "99"
    transPrice = "10"

    @pytest.mark.dependency(depends = ["TestCase::test_login"])
    @pytest.mark.parametrize("login", params, indirect=True )
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
            pw = product_page.ProductPage(login)
            pw.CreateBasicProduct(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]  
            )
        ## expect = [
        #     {
        #         "productname": self.productname,
        #         "picname": self.picname,
        #         "price": self.price,
        #         "stock": self.stock,
        #         "transPrice": self.transPrice
        #     }
        # ]
        # for data in expect:
        #     pw = product_page.ProductPage()
        #     pw.CreateBasicProduct(
        #         data["productname"],
        #         data[1],
        #         data[2],
        #         data[3],
        #         data[4]
        #     )

        # for data in json.dumps(expect):


        # pw = product_page.ProductPage()
        # tip = pw.CreateBasicProduct(expect)
        pass

if __name__ == '__main__':
    pytest.main(["-vs"])