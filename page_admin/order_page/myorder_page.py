from base.base_page import BasePage
class MyOrder(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    order_url = "https://admin-tg-test.chunsutech.com/order/list"

    def AddOrder(self, ):
        self.visit(self.order_url)
        # Click button:has-text("Add Order")
        self.click("button:has-text(\"Add Order\")")

    def SearchOrder(self, search_data):
        self.visit(self.order_url)
        # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
        self.fill(".ant-input-search", search_data)
        # Click text=Add Order高级搜索 >> button >> nth=1
        self.click(".anticon-search")
        # Click [aria-label="reload"] svg
        self.click(".anticon-reload")



        