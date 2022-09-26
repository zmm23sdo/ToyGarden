import sys
sys.path.append("../")

import pytest
from page_object import login_page

class TestCase:


    @pytest.mark.dependency()
    def test_login(self):
        expect = [
            ("admin", "qwer@1234", "登录成功！")]

        for data in expect:
            pw = login_page.LoginPage()
            tip = pw.login(data[0], data[1])
            assert tip == data[2]

    # def test_loginerror(self):
    #     expect = [
    #         ("", "", "登录成功！"),
    #         ("abc","qwer@1234","登录成功！"),
    #         ("admin","qwer1234","登录成功！")]

    #     for data in expect:
    #         pw = login_page.LoginPage()
    #         tip = pw.login(data[0], data[1])
    #         assert tip != data[2]

