from base import base_page

class LoginPage(base_page.BasePage):
    admin_url = "https://admin-tg-test.chunsutech.com/"
    locater_username = "#user_name"
    locater_password = "#password"
    button_in = ".ant-btn.ant-btn-primary.ant-btn-lg"
    bubble = ".ant-message-notice-content"

    def __init__(self) -> None:
        super().__init__()
        self.open()

    def login(self, username, password):
        self.visit(self.admin_url)

        self.locator(self.locater_username).fill(username)
        self.locator(self.locater_password).fill(password)

          # Click button:has-text("登 录")
        self.locator(self.button_in).click()
        # assert page.url == "https://admin-tg-dev.chunsutech.com/dashboard"
        # Click .ant-message-notice-content
        self.locator(self.bubble).click()

        tip = self.page.text_content(self.bubble)

        return tip


