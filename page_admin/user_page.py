from base.base_page import BasePage

class UserPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    user_url = "https://admin-tg-test.chunsutech.com/users/users"
    create_button = ".ant-btn.ant-btn-primary"
    username_text = "#username"
    fullname_text = "#name"
    email_text = "#email"
    role_selector = ".ant-select-selection-overflow"
    role_selector_option = "#role_ids_list"
    password_text = "#password"   
    confirm_button = ".ant-space-item>.ant-btn.ant-btn-primary" 

    def CreateUser(self, username, fullname, email, password):
        # Go to https://admin-tg-test.chunsutech.com/users/users
        self.visit(self.user_url)
        # Click button:has-text("Create User")
        self.click(self.create_button)
        # Fill [placeholder="\35 -15 alphabets or numbers"]
        self.fill(self.username_text, username)
        # Fill text=Fullname0 / 32 >> [placeholder="请输入"]
        self.fill(self.fullname_text, fullname)
        # Fill #email
        self.fill(self.email_text, email)
        # Click .ant-select-selector
        self.click(self.role_selector)
        # Click .ant-select-dropdown
        self.click(self.role_selector_option)
        '''
        need Role finished
        '''
        # Fill input[type="password"]
        self.fill(self.password_text, password)
        # Click button:has-text("确 定")
        self.click(self.confirm_button)

    search_text = ".ant-input-wrapper.ant-input-group"
    search_button = ".ant-btn.ant-btn-default.ant-btn-icon-only.ant-input-search-button"
    reload_svg = ".anticon.anticon-reload"

    def SearchUser(self, search_data):
        # Go to https://admin-tg-test.chunsutech.com/users/users
        self.visit(self.user_url)
        # Fill [placeholder="commodity\.list\.search\.placeholder"]
        self.fill(self.search_text, search_data)
        # Click button >> nth=1
        self.click(self.search_button)
        # Click [aria-label="reload"] svg
        self.click(self.reload_svg)

    


