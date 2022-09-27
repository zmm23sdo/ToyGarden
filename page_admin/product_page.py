from base import base_page

class ProductPage(base_page.BasePage):
    
    product_url = "https://admin-tg-test.chunsutech.com/product/list"
    create_button = ".space___lok53>.ant-space-item>.ant-btn.ant-btn-primary"
    productname_text = "#name"
    describe_text = "#describe"
    pic_input = "#pic"
    price_text = "#price"
    stock_text = "#stock"

    transPrice_text = "#transPrice"
    location_select = "#location"
    location_label = ".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active"
    button_submit = ".ant-btn.ant-btn-primary"

    bubble = ".ant-message-notice-content"

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    def CreateBasicProduct(self, productname, picname, price,
                       stock, transPrice):
        # Go to https://admin-tg-test.chunsutech.com/product/list
        self.visit(self.product_url)
        # Click button:has-text("Add Product")
        # self.locator(self.create_button).click()
        self.click(self.create_button)
        # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
        self.locator(self.productname_text).fill(productname)
        # Upload BananaClientCode.txt
        # self.locator(self.pic_input).set_input_files(picname)
        self.input(self.pic_input, picname)
        ##
        self.wait(10000)
        # Fill text=价格RM >> [placeholder="请输入"]
        # self.locator(self.price_text).fill(price)
        self.fill(self.price_text, price)
        # Fill #stock
        # self.locator(self.stock_text).fill(stock)
        self.fill(self.stock_text, stock)
        # Fill text=Unified The FreightRM >> [placeholder="请输入"]
        # self.locator(self.transPrice_text).fill(transPrice)
        self.fill(self.transPrice_text, transPrice)
        # Click .ant-select.ant-select-in-form-item.ant-select-status-error .ant-select-selector
        # self.locator(self.location_select).click()
        self.click(self.location_select)
        # Click text=Selangor >> nth=1
        # self.locator(self.location_label).click()
        self.click(self.location_label)
        # Click button:has-text("Save and Publish")
        # self.locator(self.button_submit).click()
        self.click(self.button_submit)
        # # Click .ant-message-notice-content
        # self.locator(self.bubble).click()

        # tip = self.page.text_content(self.bubble)
