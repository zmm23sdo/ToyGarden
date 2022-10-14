from base.base_page import BasePage

class SpecificationPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    specification_url = "https://admin-tg-test.chunsutech.com/product/specification"
    createspecification_button = "button:has-text(\"添加商品属性\")"
    specification_name_text = "#name"
    specType_selector = "#specType"
    specType_list_0 = "#specType_list_0"
    options_text = ".ant-input.optionInput___BiyrP"
    # add_options_button = ".ant-input.optionInput___BiyrP"
    submit_button = ".ant-btn.ant-btn-primary"


    def CreateSpecification(self, specification_name, options):
        # Go to https://admin-tg-test.chunsutech.com/product/specification
        self.visit(self.specification_url)
        # Click button:has-text("添加商品属性") >> nth=0
        self.locator(self.createspecification_button).first.click()
        # assert page.url == "https://admin-tg-test.chunsutech.com/product/specification/create"
        # Fill [placeholder="请输入"]
        self.fill(self.specification_name_text, specification_name)
        # Click input[role="combobox"]
        self.click(self.specType_selector)
        # Click text=Radio
        self.click(self.specType_list_0)
        # Fill text=OptionsAdd Options >> input[type="text"]
        self.fill(self.options_text, options)
        # Click button:has-text("提 交")
        self.click(self.submit_button)

    createspecificationset_button = "button:has-text(\"添加商品属性集\")"
    specificationset_name_text = "#name"
    specificationset_selector = ".ant-select-selection-overflow"
    specificationset_option = ".ant-select-item"
    add_specificationset_option = "button:has-text(\"添加商品字段\")"
    page_body = ".ant-pro-basicLayout-has-header"
    submit_set_button = ".ant-space>.ant-space-item>.ant-btn-primary"
    bubble_button = ".ant-message-notice-content"

    def CreateSpecificationSet(self, specificationset_name):
        # Go to https://admin-tg-test.chunsutech.com/product/specification
        self.visit(self.specification_url)
        # Click button:has-text("添加商品属性集")
        self.click(self.createspecificationset_button)
        # assert page.url == "https://admin-tg-test.chunsutech.com/product/specification/set/create"
        # Fill [placeholder="请输入"]
        self.fill(self.specificationset_name_text, specificationset_name)
        # Click .ant-select-selection-overflow
        self.click(self.specificationset_selector)
        # Click text=Specification name >> nth=0
        self.locator(self.specificationset_option).first.click()
        # Click text=属性字段
        self.click(self.page_body)
        # Click button:has-text("提 交")
        self.click(self.submit_set_button)
        # Click .ant-message-notice-content
        self.click(self.bubble_button)

    attributes_name_text = ".ant-input-affix-wrapper.ant-input-affix-wrapper-status-success>#name"
    attributes_options_text = ".optionContainer___3DhqF>.ant-input"
    confirm_button = "button:has-text(\"确 定\")"
        
    def CreateSpecificationSetAddAttributes(self, attributes_name, options):
        # Click button:has-text("添加商品字段")
        self.click(self.add_specificationset_option)
        # Fill text=NameType请选择 >> [placeholder="请输入"]
        self.fill(self.attributes_name_text, attributes_name)
        # Click text=Type请选择 >> input[role="combobox"]
        self.click(self.specType_selector)
        # Click text=RadioCheck >> div >> nth=0
        self.click(self.specType_list_0)
        # Fill text=OptionsAdd Options >> input[type="text"]
        self.fill(self.attributes_options_text, options)
        # Click button:has-text("确 定")
        self.click(self.confirm_button)
        # Click .ant-message-notice-content
        self.click(self.bubble_button)




