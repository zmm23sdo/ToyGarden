test_url = "https://admin-tg-test.chunsutech.com/"
dev_url = "https://admin-tg-dev.chunsutech.com/"
path = "user/login/"
locater_username = "#user_name"
locater_password = "#password"
button_in = ".ant-btn.ant-btn-primary.ant-btn-lg"
bubble = ".ant-message-notice-content"

dashboard_url = "https://admin-tg-dev.chunsutech.com/dashboard"
header_span = ".ant-dropdown-trigger.action___LP4_P.account___6HXOq"
logout_li = ".ant-dropdown-menu-item"


def adminLogin(page, username, password):
    # Go to https://admin-tg-dev.chunsutech.com/user/login/
    page.goto(dev_url+path)
    # Fill #username
    page.locator(locater_username).fill(username)
    # Fill input[type="password"]
    page.locator(locater_password).fill(password)
    # Click button:has-text("登 录")
    page.locator(button_in).click()
    # assert page.url == "https://admin-tg-dev.chunsutech.com/dashboard"
    # Click .ant-message-notice-content
    page.locator(bubble).click()

def adminLogout(page):
    # Go to https://admin-tg-dev.chunsutech.com/dashboard
    page.goto(dashboard_url)
    # Click span:has-text("Serati Ma") >> nth=0
    page.locator(header_span).click()
    # Click 退出登录
    page.locator(logout_li).click()
