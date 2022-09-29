from base import base_page

class LoginPage(base_page.BasePage):
    admin_url = "https://admin-tg-test.chunsutech.com/"
    locater_username = "#user_name"
    locater_password = "#password"
    button_in = ".ant-btn.ant-btn-primary.ant-btn-lg"
    bubble = ".ant-message-notice-content"
    dashboard_url = "https://admin-tg-test.chunsutech.com/dashboard"
    header_icon = ".ant-dropdown-trigger.action___LP4_P.account___6HXOq"
    logout_button = ".ant-dropdown-menu-item"

    def __init__(self) -> None:
        super().__init__()
        self.open()

    def login(self, username, password):
        self.visit(self.admin_url)
        self.fill(self.locater_username, username)
        self.fill(self.locater_password, password)
          # Click button:has-text("登 录")
        self.click(self.button_in)
        # assert page.url == "https://admin-tg-dev.chunsutech.com/dashboard"
        # Click .ant-message-notice-content
        self.click(self.bubble)
        tip = self.page.text_content(self.bubble)
        return tip
    
    error_user_text = "text=用户名是必填项！"
    error_pwd_text = "text=密码是必填项！"

    def login_empty(self, username, password):
        self.visit(self.admin_url)
        self.fill(self.locater_username, username)
        self.fill(self.locater_password, password)
          # Click button:has-text("登 录")
        self.click(self.button_in)
        # Click text=用户名是必填项！
        self.click(self.error_user_text)
        # Click text=密码是必填项！
        self.click(self.error_pwd_text)
        tip_user = self.page.text_content(self.error_user_text)
        tip_pwd = self.page.text_content(self.error_pwd_text)
        return tip_user, tip_pwd
        
    def login_empty_username(self, username, password):
        self.visit(self.admin_url)
        self.fill(self.locater_username, username)
        self.fill(self.locater_password, password)
          # Click button:has-text("登 录")
        self.click(self.button_in)
        # Click text=用户名是必填项！
        self.click(self.error_user_text)
        # # Click text=密码是必填项！
        # self.click(self.error_pwd_text)
        tip_user = self.page.text_content(self.error_user_text)
        # tip_pwd = self.page.text_content(self.error_pwd_text)
        return tip_user

    def login_empty_password(self, username, password):
        self.visit(self.admin_url)
        self.fill(self.locater_username, username)
        self.fill(self.locater_password, password)
          # Click button:has-text("登 录")
        self.click(self.button_in)
        # # Click text=用户名是必填项！
        # self.click(self.error_user_text)
        # Click text=密码是必填项！
        self.click(self.error_pwd_text)
        # tip_user = self.page.text_content(self.error_user_text)
        tip_pwd = self.page.text_content(self.error_pwd_text)
        return tip_pwd

    def loginout(self):
        self.visit(self.dashboard_url)
        self.click(self.header_icon)
        self.click(self.logout_button)
        # assert page.url == "https://admin-tg-test.chunsutech.com/user/login?redirect=%2Fdashboard"