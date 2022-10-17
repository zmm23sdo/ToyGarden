from base.base_page import BasePage

class UserPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    def CreateUser(self, username, fullname, email, password):
        # Go to https://admin-tg-test.chunsutech.com/users/users
        self.visit(self.user_url)
        # Click button:has-text("Create User")
        self.click(".ant-btn.ant-btn-primary")
        # Fill [placeholder="\35 -15 alphabets or numbers"]
        self.fill("#username", username)
        # Fill text=Fullname0 / 32 >> [placeholder="请输入"]
        self.fill("#email", fullname)
        # Fill #email
        self.fill("#email", email)
        # Click .ant-select-selector
        self.click(".ant-select-selection-overflow")
        # Click .ant-select-dropdown
        self.click("#role_ids_list")
        '''
        need Role finished
        '''
        # Fill input[type="password"]
        self.fill("#password", password)
        # Click button:has-text("确 定")
        self.click(".ant-space-item>.ant-btn.ant-btn-primary" )