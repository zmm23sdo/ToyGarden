import os
import sys

from page_admin.product_page import myproduct_page
sys.path.append(os.getcwd())

import pytest
from page_admin import login_page
from faker import Faker

class TestAdminLogin:
    
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

    def test_login_empty_username(self):
        pw = login_page.LoginPage()
        expect = [
            {
                "username":"",
                "password":"admin",
                "error":"用户名是必填项！"
            }
        ]
        tip_user = pw.login_empty_username(expect[0]['username'],expect[0]['password'])
        assert tip_user == expect[0]['error']
            
    def test_login_empty_password(self):
        pw = login_page.LoginPage()
        expect = [
            {
                "username":"admin",
                "password":"",
                "error":"密码是必填项！"
            }
        ]
        tip_user = pw.login_empty_password(expect[0]['username'],expect[0]['password'])
        assert tip_user == expect[0]['error']



if __name__ == '__main__':
    pytest.main(["cases/test_auth.py","-vs"])