from base.base_page import BasePage

class ShipmentTemplatePage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    template_url = "https://admin-tg-test.chunsutech.com/shipment/template"

    def AddShippingTemplate(self, templatename, weight, freight,  continuation, renewal):
        self.visit(self.template_url)
        # Click button:has-text("添加运费模版")
        self.click("button:has-text(\"添加运费模版\")")
        #
        self.wait(3000)
        # Fill [placeholder="请输入"]
        self.fill("#templateName", templatename)
        # Click text=按件数
        self.click("text=按件数")
        # Click text=按重量
        # self.click("text=按重量")
        # Click button:has-text("指定可配送区域和运费")
        self.click("button:has-text(\"指定可配送区域和运费\")")
            # Click text=Johor
        self.click("text=Johor")
        # Click text=Kuala Lumpur
        self.click("text=Kuala Lumpur")
        # Click text=Negeri Sembilan
        self.click("text=Negeri Sembilan")
        # Click text=Perak
        self.click("text=Perak")
        # Click text=Sabah
        self.click("text=Sabah")
        # Click text=Selangor
        self.click("text=Selangor")
        # Click text=Kedah
        self.click("text=Kedah")
        # Click text=Labuan
        self.click("text=Labuan")
        # Click text=Pahang
        self.click("text=Pahang")
        # Click text=Perlis
        self.click("text=Perlis")
        # Click text=Sarawak
        self.click("text=Sarawak")
        # Click text=Kelantan
        self.click("text=Kelantan")
        # Click text=Melaka
        self.click("text=Melaka")
        # Click text=Penang
        self.click("text=Penang")
        # Click text=Putrajaya
        self.click("text=Putrajaya")
        # Click text=Terengganu
        self.click("text=Terengganu")
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
        # Fill [placeholder="请输入"] >> nth=1
        self.locator("[placeholder=\"请输入\"]").nth(1).fill(weight)
        # Fill [placeholder="请输入"] >> nth=2
        self.locator("[placeholder=\"请输入\"]").nth(2).fill(freight)
        # Fill [placeholder="请输入"] >> nth=3
        self.locator("[placeholder=\"请输入\"]").nth(3).fill(continuation)
        # Fill [placeholder="请输入"] >> nth=4
        self.locator("[placeholder=\"请输入\"]").nth(4).fill(renewal)
        # Click text=保存
        self.click("text=保存")
        # Click button:has-text("Submit")
        self.click("button:has-text(\"Submit\")")
###################################################################
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip
####################################################################

    def EditShippingTemplate(self, templatename, weight, freight,  continuation, renewal):
        # self.visit(self.template_url)
        # Click button:has-text("Edit") >> nth=0
        self.locator("button:has-text(\"Edit\")").first.click()

    def DeleteShippingTemplate(self, templatename, weight, freight,  continuation, renewal):
        # self.visit(self.template_url)
        # Click button:has-text("Delete") >> nth=0
        self.locator("button:has-text(\"Delete\")").first.click()
    
    def ModifySetting(self):
        # Click text=按商品累加运费
        # self.click("text=按商品累加运费")
        # Click text=组合运费
        self.click("text=组合运费")
        # Click button:has-text("Confirm")
        self.click("button:has-text(\"Confirm\")")
###################################################################
        self.click(".ant-message-notice-content")
        tip = self.page.text_content( ".ant-message-notice-content")
        return tip
####################################################################

    def SearchShippingTemplate(self, search_data):
        self.visit(self.template_url)
        # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
        self.fill(".ant-input-search", search_data)


    def AddPickup(self):
        self.visit(self.template_url)
        # Click text=上门自提
        self.click("text=上门自提")
        # Click button:has-text("添加自提点")
        self.click("button:has-text(\"添加自提点\")")

    def SearchPickup(self, search_data):
        self.visit(self.template_url)
        # Click text=上门自提
        self.click("text=上门自提")
        # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
        self.fill(".ant-input-search", search_data)













    