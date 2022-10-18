from base.base_page import BasePage

class ShopDecorationPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    shop_decoration_url = "https://admin-tg-test.chunsutech.com/shop/decoration"

    def AddCarousel(self, pic_name):
        # Go to https://admin-tg-test.chunsutech.com/shop/decoration
        self.visit(self.shop_decoration_url)
        # Click span[role="button"]:has-text("Upload")
        self.click("span[role=\"button\"]:has-text(\"Upload\")")
        # Click text=本地上传
        self.click("text=本地上传")
        self.input(".ant-upload.ant-upload-drag.ant-upload-drag-uploading", pic_name)
        # Click button:has-text("提 交")
        self.click("button:has-text(\"提 交\")")

    def AddMultipleImages1(self):
        # Go to https://admin-tg-test.chunsutech.com/shop/decoration
        self.visit(self.shop_decoration_url)
        # Click span[role="button"]:has-text("Multiple Images-1")
        self.click("text=Multiple Images-1")

    def AddProduct(self):
        # Go to https://admin-tg-test.chunsutech.com/shop/decoration
        self.visit(self.shop_decoration_url)
        # Click span[role="button"]:has-text("Multiple Images-1")
        self.click("text=Product-By Category")

    def AddMultipleImages2(self):
        # Go to https://admin-tg-test.chunsutech.com/shop/decoration
        self.visit(self.shop_decoration_url)
        # Click span[role="button"]:has-text("Multiple Images-1")
        self.click("text=Multiple Images-2")

    def AddMultipleImagesFree(self):
        # Go to https://admin-tg-test.chunsutech.com/shop/decoration
        self.visit(self.shop_decoration_url)
        # Click span[role="button"]:has-text("Multiple Images-1")
        self.click("text=Multiple Images-Free")
