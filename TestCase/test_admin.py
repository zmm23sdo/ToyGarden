import sys
sys.path.append("../")

from playwright.sync_api import Page
from UI import admin_login
from faker import Faker
import datetime


username = "mvdev"
password = "qwer@1234"

fake = Faker()
hour = datetime.datetime.now().strftime('%H')
minute = datetime.datetime.now().strftime('%M')
sec = datetime.datetime.now().strftime('%S')



def test_admin_login(page:Page):
    admin_login.adminLogin(page, username, password)
    content = page.text_content(".ant-message-notice-content")
    assert content == "登录成功！"

# def test_admin(page:Page):
#     admin_login.adminLogin(page, username, password)
#     # Go to https://admin-tg-test.chunsutech.com/product/create/
#     page.goto("https://admin-tg-test.chunsutech.com/product/create/")
#     # Click button:has-text("Enable Variations")
#     page.locator("button:has-text(\"Enable Variations\")").click()
#     # Click button:has-text("Add Options")
#     page.locator("button:has-text(\"Add Options\")").click()
#     page.locator('input[id^="testpic_"]')
#     content = page.locator('input[id^="testpic_"]')

#     for testpic in content.element_handles():
#         print(f'\ncontent={testpic.get_attribute("id")}')
#         page.set_input_files("#"+testpic.get_attribute("id"), "/Users/zhangmingwei/Projects/ToyGarden/pic.jpeg")

    