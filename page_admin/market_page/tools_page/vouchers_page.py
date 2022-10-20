from base.base_page import BasePage
class VouchersPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    vouchers_url = "https://admin-tg-test.chunsutech.com/market/tools/vouchers"

    def AddVouchers(self, vouchaers_name, vouchers_code, amount, quantity, min_price):
        self.visit(self.vouchers_url)
        # Click button:has-text("Add Vouchers")
        self.click("button:has-text(\"Add Vouchers\")")
        self.wait(3000)
        # Fill text=Vouchers NameVoucher name is not visible to buyers >> [placeholder="请输入"]
        self.fill("#name", vouchaers_name)
        # Fill text=Vouchers CodePlease enter A-Z,0-9; 10 characters maximum >> [placeholder="请输入"]
        self.fill("#code", vouchers_code)
        # Click #period
        self.click("#period")
        # Click tbody >> text=19
        self.click("tbody >> text=19")
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
        # Click tbody >> text=20
        self.click("tbody >> text=20")
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
        # Fill text=Fix AmountRM >> [placeholder="请输入"]
        self.fill("#discAmount",amount)
        # Fill text=Usage QuantityTotal usable form all buyers >> [placeholder="请输入"]
        self.fill("#quantity", quantity)
        # Fill text=Minimum Basket PriceRM >> [placeholder="请输入"]
        self.fill("#minBasketPrice", min_price)
        # Click button:has-text("提 交")
        self.click("button:has-text(\"提 交\")")
###################################################################
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip
####################################################################

    def DeleteVochers(self):
        self.visit(self.vouchers_url)
        # Click button:has-text("Delete") >> nth=0
        self.locator("button:has-text(\"Delete\")").first.click()
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")




