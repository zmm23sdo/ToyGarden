admin_url = "https://admin-tg-test.chunsutech.com/"
path = "user/login/"
locater_username = "#username"
locater_password = "#password"
button_in = ".ant-btn.ant-btn-primary.ant-btn-lg"
bubble = ".ant-message-notice-content"
def adminLogin(page, username, password):
    # Go to https://admin-tg-test.chunsutech.com/user/login/
    page.goto(admin_url+path)
    # Fill #username
    page.locator(locater_username).fill(username)
    # Fill input[type="password"]
    page.locator(locater_password).fill(password)
    # Click button:has-text("登 录")
    page.locator(button_in).click()
    # assert page.url == "https://admin-tg-test.chunsutech.com/dashboard"
    # Click .ant-message-notice-content
    page.locator(bubble).click()
