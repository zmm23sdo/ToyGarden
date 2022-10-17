from base.base_page import BasePage

class LoginPage(BasePage):
    admin_url = "https://admin-tg-test.chunsutech.com/"
    dashboard_url = "https://admin-tg-test.chunsutech.com/dashboard"

    # locater_username = "#user_name"
    # locater_password = "#password"
    # button_in = ".ant-btn.ant-btn-primary.ant-btn-lg"
    # bubble = ".ant-message-notice-content"
    # header_icon = ".ant-dropdown-trigger.action___LP4_P.account___6HXOq"
    # logout_button = ".ant-dropdown-menu-item"

    # error_user_text = "text=用户名是必填项！"
    # error_pwd_text = "text=密码是必填项！"

    def __init__(self) -> None:
        super().__init__()
        self.open()

    def login(self, username, password):
        self.visit(self.admin_url)
        self.fill("#user_name", username)
        self.fill("#password", password)
          # Click button:has-text("登 录")
        self.click(".ant-btn.ant-btn-primary.ant-btn-lg")
        # assert page.url == "https://admin-tg-dev.chunsutech.com/dashboard"
        # Click .ant-message-notice-content
        self.click( ".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip
    
    

    def login_empty(self, username, password):
        self.visit(self.admin_url)
        self.fill("#user_name", username)
        self.fill("#password", password)
          # Click button:has-text("登 录")
        self.click(".ant-btn.ant-btn-primary.ant-btn-lg")
        # Click text=用户名是必填项！
        self.click("text=用户名是必填项！")
        # Click text=密码是必填项！
        self.click("text=密码是必填项！")
        tip_user = self.page.text_content("text=用户名是必填项！")
        tip_pwd = self.page.text_content("text=密码是必填项！")
        return tip_user, tip_pwd
        
    def login_empty_username(self, username, password):
        self.visit(self.admin_url)
        self.fill("#user_name", username)
        self.fill("#password", password)
          # Click button:has-text("登 录")
        self.click(".ant-btn.ant-btn-primary.ant-btn-lg")
        # Click text=用户名是必填项！
        self.click("text=用户名是必填项！")
        # # Click text=密码是必填项！
        # self.click("text=密码是必填项！")
        tip_user = self.page.text_content("text=用户名是必填项！")
        # tip_pwd = self.page.text_content("text=密码是必填项！")
        return tip_user

    def login_empty_password(self, username, password):
        self.visit(self.admin_url)
        self.fill("#user_name", username)
        self.fill("#password", password)
          # Click button:has-text("登 录")
        self.click(".ant-btn.ant-btn-primary.ant-btn-lg")
        # # Click text=用户名是必填项！
        # self.click("text=用户名是必填项！")
        # Click text=密码是必填项！
        self.click("text=密码是必填项！")
        # tip_user = self.page.text_content("text=用户名是必填项！")
        tip_pwd = self.page.text_content("text=密码是必填项！")
        return tip_pwd

    def loginout(self):
        self.visit("https://admin-tg-test.chunsutech.com/dashboard")
        self.click(".ant-dropdown-trigger.action___LP4_P.account___6HXOq")
        self.click(".ant-dropdown-menu-item")
        # assert page.url == "https://admin-tg-test.chunsutech.com/user/login?redirect=%2Fdashboard"