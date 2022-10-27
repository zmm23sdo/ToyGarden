from base.base_page import BasePage

class ProductPage(BasePage):
    
    product_url = "https://admin-tg-test.chunsutech.com/product/list"
    # create_button = ".space___lok53>.ant-space-item>.ant-btn.ant-btn-primary"
    # productname_text = "#name"
    # pic_input = "#pic"
    # price_text = "#price"
    # stock_text = "#stock"

    # transPrice_text = "#transPrice"
    # location_select = "#location"
    # location_label = ".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active"
    # button_submit = "button:has-text(\"Save and Publish\")"

    # bubble = ".ant-message-notice-content"

    # describe_text = "#describe"
    # attributes_add_button = "button:has-text(\"添加商品属性\")"
    # add_new_attributes_button = "button:has-text(\"Add New Attributes\")"
    # attributes_name_text = ".ant-input-affix-wrapper.ant-input-affix-wrapper-status-success>#name"
    # attributes_type_select = "#type"
    # attributes_type_select_spn = ".ant-select-item-option-active"
    # attributes_add_confirm = "button:has-text(\"确 定\")"
    # attributes_checkbox = ".ant-table-selection-extra"
    # add_new_attributes_submit = ".actionSpace___3jAvb>.ant-space-item>.ant-btn.ant-btn-primary"

    # enable_variations_button = "button:has-text(\"Enable Variations\")"
    # variations_name_text = ".variants___23orT>.ant-form-item>.ant-row.ant-form-item-row>.ant-col.ant-form-item-control>.ant-form-item-control-input>.ant-form-item-control-input-content>.ant-input-affix-wrapper.pro-field.pro-field-md>.ant-input"
    # options_name_text = ".optionContainer___3DhqF>.ant-form-item>.ant-row.ant-form-item-row>.ant-col.ant-form-item-control>.ant-form-item-control-input>.ant-form-item-control-input-content>.ant-input-affix-wrapper.pro-field.pro-field-md"
    # addoption_button = "fieldset>.ant-btn.ant-btn-default"
    # pic_option = 'input[id^="testpic_"]'
    # options_add_text = "[placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:Red\\,etc\\.\"]"
    # price_box = ".variantInfo___1m5bJ>.ant-input-number-affix-wrapper>.ant-input-number>.ant-input-number-input-wrap>.ant-input-number-input"
    


    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    def CreateBasicProduct(self, productname, picname, price,
                       stock, transPrice):
        # Go to https://admin-tg-test.chunsutech.com/product/list
        self.visit(self.product_url)
        # Click button:has-text("Add Product")
        # self.locator("button:has-text(\"Add Product\")").click()
        self.click("button:has-text(\"Add Product\")")
        # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
        self.locator("#name").fill(productname)
        # Upload BananaClientCode.txt
        # self.input("span[role=\"button\"]:has-text(\"Upload\")",picname)
        # Click span[role="button"]:has-text("Upload")
        self.click("span[role=\"button\"]:has-text(\"Upload\")")
        # Click text=本地上传
        self.click("text=本地上传")
        ##
        # self.wait(10000)
        # self.locator("#pic").set_input_files(picname)
        # self.input(".ant-upload.ant-upload-btn", picname)
        self.input(".ant-upload.ant-upload-btn>input", picname)
        self.wait(10000)
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
        # ##
        # self.wait(10000)
        # Fill text=价格RM >> [placeholder="请输入"]
        # self.locator("#price").fill(price)
        self.fill("#price", price)
        # Fill #stock
        # self.locator("#stock").fill(stock)
        self.fill("#stock", stock)
        # Fill text=Unified The FreightRM >> [placeholder="请输入"]
        # self.locator("#transPrice").fill(transPrice)
        self.fill("#transPrice", transPrice)
        # Click .ant-select.ant-select-in-form-item.ant-select-status-error .ant-select-selector
        # self.locator("#location").click()
        self.click("#location")
        # Click text=Selangor >> nth=1
        # self.locator(".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active").click()
        self.click(".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active")
        # Click button:has-text("Save and Publish")
        # self.locator("button:has-text(\"Save and Publish\")").click()
        self.click("button:has-text(\"Save and Publish\")")
        # # Click .ant-message-notice-content
        # self.locator(".ant-message-notice-content").click()
        # tip = self.page.text_content(".ant-message-notice-content")

    def CreateAdvanceProdut(self, productname, describe, picname, picname1, picname2,
                            picname3, picname4, picname5, picname6, picname7, picname8,
                            picname9, attributes_name, variation_name, options_name,
                            pic_url, option_name1, option_name2, option_name3, price,
                            stock, weight, sku, barcode, sizeX, sizeY, sizeZ, spu
                            ):
        # Go to https://admin-tg-test.chunsutech.com/product/list
        self.visit(self.product_url)
        # Click button:has-text("Add Product")
        # self.locator("button:has-text(\"Add Product\")").click()
        self.click("button:has-text(\"Add Product\")")
        # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
        #商品名称
        self.locator("#name").fill(productname)
        # Fill textarea
        #商品描述
        self.locator("#describe").fill(describe)
        # self.locator("#pic").set_input_files(picname)
        #商品图片
        self.input("#pic", picname)
        self.wait(10000)
        self.input("#pic", picname1)
        self.wait(10000)
        self.input("#pic", picname2)
        self.wait(10000)
        self.input("#pic", picname3)
        self.wait(10000)
        self.input("#pic", picname4)
        self.wait(10000)
        self.input("#pic", picname5)
        self.wait(10000)
        self.input("#pic", picname6)
        self.wait(10000)
        self.input("#pic", picname7)
        self.wait(10000)
        self.input("#pic", picname8)
        self.wait(10000)
        self.input("#pic", picname9)
        self.wait(10000)
        #添加商品属性
        # Click button:has-text("添加商品属性")
        self.click("button:has-text(\"添加商品属性\")")
        #add new attributes
        # Click button:has-text("Add New Attributes")
        self.click("button:has-text(\"Add New Attributes\")")
        # Fill text=NameType请选择 >> [placeholder="请输入"]
        self.fill(".ant-input-affix-wrapper.ant-input-affix-wrapper-status-success>#name", attributes_name)
        # Click text=Type请选择 >> input[role="combobox"]
        self.click("#type")
        # Click .ant-select-item >> nth=0
        self.click(".ant-select-item-option-active")
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")
        # Click div[role="alert"]:has-text("已选择1项 取消选择")
        self.click(".ant-table-selection-extra")
        # Click button:has-text("Submit")
        self.click(".actionSpace___3jAvb>.ant-space-item>.ant-btn.ant-btn-primary")
        #添加变体
        # Click button:has-text("Enable Variations")
        self.click("button:has-text(\"Enable Variations\")")
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:colour\,etc\."]
        self.fill(".variants___23orT>.ant-form-item>.ant-row.ant-form-item-row>.ant-col.ant-form-item-control>.ant-form-item-control-input>.ant-form-item-control-input-content>.ant-input-affix-wrapper.pro-field.pro-field-md>.ant-input", variation_name)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."]
        self.fill(".optionContainer___3DhqF>.ant-form-item>.ant-row.ant-form-item-row>.ant-col.ant-form-item-control>.ant-form-item-control-input>.ant-form-item-control-input-content>.ant-input-affix-wrapper.pro-field.pro-field-md", options_name)
        self.locator("fieldset>.ant-btn.ant-btn-default").click(click_count=3)
        # page.locator(pic_option)
        content = self.locator('input[id^="testpic_"]')
        for testpic in content.element_handles():
            print(f'\ncontent={testpic.get_attribute("id")}')
            self.input("#"+testpic.get_attribute("id"), pic_url)
        self.wait(10000)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."] >> nth=1
        self.locator("[placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:Red\\,etc\\.\"]").nth(1).fill(option_name1)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."] >> nth=2
        self.locator("[placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:Red\\,etc\\.\"]").nth(2).fill(option_name2)
        # Fill [placeholder="Enter\ Vairation\ Name\,eg\:Red\,etc\."] >> nth=3
        self.locator("[placeholder=\"Enter\\ Vairation\\ Name\\,eg\\:Red\\,etc\\.\"]").nth(3).fill(option_name3)
        self.wait(10000)
        # Fill [placeholder="Price"]
        self.fill(".variantInfo___1m5bJ>.ant-input-number-affix-wrapper>.ant-input-number>.ant-input-number-input-wrap>.ant-input-number-input", price)
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
