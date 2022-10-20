from base.base_page import BasePage

class SubscriptionPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    subscription_url = "https://admin-tg-test.chunsutech.com/customer/subscription"

    def AddSubscriptionEmail(self, email):
        self.visit(self.subscription_url)
        # Click button:has-text("Add Subscription Email")
        self.click("button:has-text(\"Add Subscription Email\")")
        # Fill text=Add Subscription EmailEmail取 消确 定 >> [placeholder="请输入"]
        self.fill("#email", email)
        # Click button:has-text("确 定") >> nth=0
        self.locator("button:has-text(\"确 定\")").first.click()#   Confirm
        # Click .ant-message-notice-content
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip

    def SearchSubscription(self, search_data):
        self.visit(self.subscription_url)
        # Fill text=Add Subscription EmailExport >> [placeholder="请输入"]
        self.fill("#search", search_data)
####################################################
        # Click button >> nth=1
        self.click(".ant-input-group-addon")
        # Click [aria-label="reload"] svg
        self.click(".anticon.anticon-reload")
####################################################

    def SubscriptSubscription(self):
        # Click button:has-text("Subscript") >> nth=1
        self.locator("button:has-text(\"Subscript\")").nth(1).click()
        # Click button:has-text("确 定") >> nth=1
        self.locator("button:has-text(\"确 定\")").nth(1).click()
        # Click .ant-message-notice-content
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip

    def CancelSubscriptSubscription(self):
        # Click button:has-text("Cancel Subscription") >> nth=0
        self.locator("button:has-text(\"Cancel Subscription\")").first.click()
        # Click button:has-text("确 定") >> nth=1
        self.locator("button:has-text(\"确 定\")").nth(1).click()
        # Click .ant-message-notice-content
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip

    def DeleteSubscriptSubscription(self):
        # Click button:has-text("Delete") >> nth=0
        self.locator("button:has-text(\"Delete\")").first.click()
        # Click button:has-text("确 定") >> nth=1
        self.locator("button:has-text(\"确 定\")").nth(1).click()
        # Click .ant-message-notice-content
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip