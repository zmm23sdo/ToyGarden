import sys
sys.path.append("../")

from playwright.sync_api import Page
from UI import admin_login
from faker import Faker
import datetime


# username = "mvdev"
username = "admin"
password = "qwer@1234"

fake = Faker()
hour = datetime.datetime.now().strftime('%H')
minute = datetime.datetime.now().strftime('%M')
sec = datetime.datetime.now().strftime('%S')



# def test_admin_login(page:Page):
#     admin_login.adminLogin(page, username, password)
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "登录成功！"

# variation_span = "button:has-text(\"Enable Variations\")"
# variation0_text = "[placeholder=\"Enter Vairation Name\\,eg\\:colour\\,etc\\.\"]"
# addoption_button = "button:has-text(\"Add Options\")"
# pic_option = 'input[id^="testpic_"]'
# pic_url ="/Users/zhangmingwei/Projects/ToyGarden/pic.jpeg"

# def test_admin(page:Page):
#     admin_login.adminLogin(page, username, password)
#     # Go to https://admin-tg-test.chunsutech.com/product/create/
#     page.goto("https://admin-tg-test.chunsutech.com/product/create/")
#     # Click button:has-text("Enable Variations")
#     page.locator(variation_span).click()
#     # Click button:has-text("Add Options")
#     # page.pause()
#     page.locator(addoption_button).click()
#     page.locator(addoption_button).click()
#     page.locator(addoption_button).click()
#     # page.locator(pic_option)
#     content = page.locator(pic_option)

#     for testpic in content.element_handles():
#         print(f'\ncontent={testpic.get_attribute("id")}')
#         page.set_input_files("#"+testpic.get_attribute("id"), pic_url)




    