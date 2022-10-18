from base.base_page import BasePage

class ProductPage(BasePage):
    
    product_url = "https://admin-tg-test.chunsutech.com/product/list"
    create_button = ".space___lok53>.ant-space-item>.ant-btn.ant-btn-primary"
    productname_text = "#name"
    pic_input = "#pic"
    price_text = "#price"
    stock_text = "#stock"

    transPrice_text = "#transPrice"
    location_select = "#location"
    location_label = ".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active"
    button_submit = ".ant-btn.ant-btn-primary"

    bubble = ".ant-message-notice-content"

    describe_text = "#describe"
    attributes_add_button = "button:has-text(\"添加商品属性\")"
    add_new_attributes_button = ".ant-space.ant-space-horizontal.ant-space-align-center.space___lok53>.ant-space-item>.ant-btn.ant-btn-primary"
    attributes_name_text = ".ant-input-affix-wrapper.ant-input-affix-wrapper-status-success>#name"
    attributes_type_select = "#type"
    attributes_type_select_spn = ".ant-select-item-option-active"
    attributes_add_confirm = "button:has-text(\"确 定\")"
    attributes_checkbox = ".ant-table-selection-extra"
    add_new_attributes_submit = ".actionSpace___3jAvb>.ant-space-item>.ant-btn.ant-btn-primary"

    enable_variations_button = "button:has-text(\"Enable Variations\")"
    variations_name_text = ".variants___23orT>.ant-form-item>.ant-row.ant-form-item-row>.ant-col.ant-form-item-control>.ant-form-item-control-input>.ant-form-item-control-input-content>.ant-input-affix-wrapper.pro-field.pro-field-md>.ant-input"
    options_name_text = ".optionContainer___3DhqF>.ant-form-item>.ant-row.ant-form-item-row>.ant-col.ant-form-item-control>.ant-form-item-control-input>.ant-form-item-control-input-content>.ant-input-affix-wrapper.pro-field.pro-field-md"
    addoption_button = "fieldset>.ant-btn.ant-btn-default"
    pic_option = 'input[id^="testpic_"]'
    options_add_text = "[placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:Red\\,etc\\.\"]"
    price_box = ".variantInfo___1m5bJ>.ant-input-number-affix-wrapper>.ant-input-number>.ant-input-number-input-wrap>.ant-input-number-input"
    


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

    def CreateAdvanceProdut(self, productname, describe, picname, picname1, picname2,
                            picname3, picname4, picname5, picname6, picname7, picname8,
                            picname9, attributes_name, variation_name, options_name,
                            pic_url, option_name1, option_name2, option_name3, price,
                            stock, weight, sku, barcode, sizeX, sizeY, sizeZ, spu
                            ):
        # Go to https://admin-tg-test.chunsutech.com/product/list
        self.visit(self.product_url)
        # Click button:has-text("Add Product")
        # self.locator(self.create_button).click()
        self.click(self.create_button)
        # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
        #商品名称
        self.locator(self.productname_text).fill(productname)
        # Fill textarea
        #商品描述
        self.locator(self.describe_text).fill(describe)
        # self.locator(self.pic_input).set_input_files(picname)
        #商品图片
        self.input(self.pic_input, picname)
        self.wait(10000)
        self.input(self.pic_input, picname1)
        self.wait(10000)
        self.input(self.pic_input, picname2)
        self.wait(10000)
        self.input(self.pic_input, picname3)
        self.wait(10000)
        self.input(self.pic_input, picname4)
        self.wait(10000)
        self.input(self.pic_input, picname5)
        self.wait(10000)
        self.input(self.pic_input, picname6)
        self.wait(10000)
        self.input(self.pic_input, picname7)
        self.wait(10000)
        self.input(self.pic_input, picname8)
        self.wait(10000)
        self.input(self.pic_input, picname9)
        self.wait(10000)
        #添加商品属性
        # Click button:has-text("添加商品属性")
        self.click(self.attributes_add_button)
        #add new attributes
        # Click button:has-text("Add New Attributes")
        self.click(self.add_new_attributes_button)
        # Fill text=NameType请选择 >> [placeholder="请输入"]
        self.fill(self.attributes_name_text, attributes_name)
        # Click text=Type请选择 >> input[role="combobox"]
        self.click(self.attributes_type_select)
        # Click .ant-select-item >> nth=0
        self.click(self.attributes_type_select_spn)
        # Click button:has-text("确 定")
        self.click(self.attributes_add_confirm)
        # Click div[role="alert"]:has-text("已选择1项 取消选择")
        self.click(self.attributes_checkbox)
        # Click button:has-text("Submit")
        self.click(self.add_new_attributes_submit)
        #添加变体
        # Click button:has-text("Enable Variations")
        self.click(self.enable_variations_button)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:colour\,etc\."]
        self.fill(self.variations_name_text, variation_name)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."]
        self.fill(self.options_name_text, options_name)
        self.locator(self.addoption_button).click(click_count=3)
        # page.locator(pic_option)
        content = self.locator(self.pic_option)
        for testpic in content.element_handles():
            print(f'\ncontent={testpic.get_attribute("id")}')
            self.input("#"+testpic.get_attribute("id"), pic_url)
        self.wait(10000)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."] >> nth=1
        self.locator(self.options_add_text).nth(1).fill(option_name1)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."] >> nth=2
        self.locator(self.options_add_text).nth(2).fill(option_name2)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."] >> nth=3
        self.locator(self.options_add_text).nth(3).fill(option_name3)
        self.wait(10000)
        # Fill [placeholder="Price"]
        self.fill(self.price_box, price)
        # Fill [placeholder="Stock"] ".variantInfo___1m5bJ>.ant-input-number>.ant-input-number-input-wrap"
        self.fill("[placeholder=\"Stock\"]", stock)
         # Fill [placeholder="Weight"]
        self.fill("[placeholder=\"Weight\"]", weight)
        # Fill [placeholder="SKU"]
        self.fill("[placeholder=\"SKU\"]", sku)
        # Fill [placeholder="Bar\ Code"]
        self.fill("[placeholder=\"Bar\\ Code\"]", barcode)
        # Click button:has-text("Apply To All")
        self.click("button:has-text(\"Apply To All\")")
         # Fill text=尺寸cm >> [placeholder="请输入"]
        self.fill("#sizeX", sizeX)
        # Fill #sizeY
        self.fill("#sizeY", sizeY)
        # Fill #sizeZ
        self.fill("#sizeZ", sizeZ)
        # Fill #spu
        self.fill("#spu", spu)
