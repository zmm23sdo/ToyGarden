from base.base_page import BasePage

class ShipmentCompanyPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    cpmpany_url = "https://admin-tg-test.chunsutech.com/shipment/company"

    def AddCompany(self, companyname, picname):
        self.visit(self.cpmpany_url)
        # Click button:has-text("添加物流公司")
        self.click("button:has-text(\"添加物流公司\")")
        # Fill [placeholder="请输入"]
        self.fill("#companyName", companyname)
        # Upload 209图片.jpeg
        self.input("#logo", picname)
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
###################################################################
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip
####################################################################

    def EditCompany(self, new_companyname, new_picname):
        self.visit(self.cpmpany_url)
        # Click button:has-text("Edit") >> nth=0
        self.locator("button:has-text(\"Edit\")").first.click()
        # Fill [placeholder="请输入"]
        self.fill("#companyName", new_companyname)
        # Upload 209图片.jpeg
        self.input("#logo", new_picname)
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
###################################################################
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip
####################################################################

    def DeleteCompany(self):
        self.visit(self.cpmpany_url)
        # Click button:has-text("Delete") >> nth=0
        self.locator("button:has-text(\"Delete\")").first.click()
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
###################################################################
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip
####################################################################


