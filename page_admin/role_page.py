from base.base_page import BasePage

class RolePage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page
    

    role_url = "https://admin-tg-test.chunsutech.com/users/roles"
    role_create_url = "https://admin-tg-test.chunsutech.com/users/roles/create"
    create_button = ".ant-btn.ant-btn-primary"
    rolename_text = "#name"
    description_text = "#description"
    all_checkbox = ".ant-checkbox-input"
    confirm_button = ".confirm___G2-JO"
    feedback_bubble = ".ant-message-notice-content"

    def CreateRole(self, rolename, description):
        # Go to https://admin-tg-test.chunsutech.com/users/roles
        self.visit(self.role_url)
        # Click button:has-text("Create Role")
        self.click(self.create_button)
        self.wait(3000)
        # Fill [placeholder="Cannot exceed 30 characters"]
        self.fill(self.rolename_text, rolename)
        # Fill textarea:has-text("role")
        self.fill(self.description_text, description)
        # Check input[type="checkbox"]
        self.locator(self.all_checkbox).check()
        # Click button:has-text("confirm")
        self.click(self.confirm_button)
        # Click .ant-message-notice-content
        self.click(self.feedback_bubble)

    search_text = ".ant-input-wrapper.ant-input-group"
    search_button = ".ant-input-group-addon"
    reload_svg = ".anticon.anticon-reload"

    def SearchRole(self, search_data):
        # Fill [placeholder="commodity\.list\.search\.placeholder"]
        self.fill(self.search_text, search_data)
        # Click button >> nth=1
        self.click(self.search_button)
        # Click [aria-label="reload"] svg
        self.click(self.reload_svg)
        

