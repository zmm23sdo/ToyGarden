from base.base_page import BasePage

class RolesPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page
    

    role_url = "https://admin-tg-test.chunsutech.com/users/roles"
    role_create_url = "https://admin-tg-test.chunsutech.com/users/roles/create"

    def CreateRole(self, rolename, description):
        # Go to https://admin-tg-test.chunsutech.com/users/roles
        self.visit(self.role_url)
        # Click button:has-text("Create Role")
        self.click(".ant-btn.ant-btn-primary")
        self.wait(3000)
        # Fill [placeholder="Cannot exceed 30 characters"]
        self.fill("#name", rolename)
        # Fill textarea:has-text("role")
        self.fill("#description", description)
        # Check input[type="checkbox"]
        self.locator(".ant-checkbox-input").check()
        # Click button:has-text("confirm")
        self.click(".confirm___G2-JO")
        # Click .ant-message-notice-content
        self.click(".ant-message-notice-content")

    def SearchRole(self, search_data):
        # Fill [placeholder="commodity\.list\.search\.placeholder"]
        self.fill(".ant-input-wrapper.ant-input-group", search_data)
        # Click button >> nth=1
        self.click(".ant-input-group-addon")
        # Click [aria-label="reload"] svg
        self.click(".anticon.anticon-reload")