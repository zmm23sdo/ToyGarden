product_url = "https://admin-tg-dev.chunsutech.com/product/list"
create_button = ".ant-btn.ant-btn-primary"
productname_text = "#name"
describe_text = "#describe"
pic_input = "#pic"
price_text = "#price"
stock_text = "#stock"


transPrice_text = "#transPrice"
location_select = "#location"
location_label = ".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active"
button_submit = ".ant-btn.ant-btn-primary"


def adminCreateBasicProduct(page, productname, picname, price,
                       stock, transPrice):
    # Go to https://admin-tg-test.chunsutech.com/product/list
    page.goto(product_url)
    # Click button:has-text("Add Product")
    page.locator(create_button).click()
    # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
    page.locator(productname_text).fill(productname)

    # Upload BananaClientCode.txt
    page.locator(pic_input).set_input_files(picname)
    ##
    page.wait_for_timeout(10000)
    # Fill text=价格RM >> [placeholder="请输入"]
    page.locator(price_text).fill(price)
    # Fill #stock
    page.locator(stock_text).fill(stock)
    # Fill text=Unified The FreightRM >> [placeholder="请输入"]
    page.locator(transPrice_text).fill(transPrice)
    # Click .ant-select.ant-select-in-form-item.ant-select-status-error .ant-select-selector
    page.locator(location_select).click()
    # Click text=Selangor >> nth=1
    page.locator(location_label).click()
    # Click button:has-text("Save and Publish")
    page.locator(button_submit).click()



button_attribute = "button:has-text(\"添加商品属性\")"
button_add = "button:has-text(\"Add New Attributes\")"
attributename_text = ".ant-modal-content #name"
type_select = "#type"
type_label = ".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active"
submit_text = "button:has-text(\"确 定\")"
svg_span = "[aria-label=\"reload\"] svg"
attributename_search = ".ant-input-wrapper.ant-input-group>.ant-input"
svg_search = ".anticon-search"
td_select = ".ant-table-row>.ant-table-cell.ant-table-selection-column"
submit_attribute = ".ant-drawer-body>.ant-space>.ant-space-item>.ant-btn.ant-btn-primary"

variation_span = "button:has-text(\"Enable Variations\")"
variation0_text = "[placeholder=\"Enter Vairation Name\\,eg\\:colour\\,etc\\.\"]"
addoption_button = "button:has-text(\"Add Options\")"
pic_option = 'input[id^="testpic_"]'
pic_url = "/Users/zhangmingwei/Projects/ToyGarden/pic.jpeg"

option_text = "[placeholder=\"Enter Vairation Name\\,eg\\:Red\\,etc\\.\"]"
addvariation_button = "button:has-text(\"Add Variation\")"
variation1_text = "text=Variation1OptionsAdd Options >> [placeholder=\"Enter Vairation Name\\,eg\\:colour\\,etc\\.\"]"
optiona_text = "text=Variation1OptionsAdd Options >> [placeholder=\"Enter Vairation Name\\,eg\\:Red\\,etc\\.\"]"
variation2_text = "text=Variation2OptionsAdd Options >> [placeholder=\"Enter Vairation Name\\,eg\\:colour\\,etc\\.\"]"
optionb_text = "text=Variation2OptionsAdd Options >> [placeholder=\"Enter Vairation Name\\,eg\\:Red\\,etc\\.\"]"
price_input = ".variantInfo___1m5bJ>.ant-input-number-affix-wrapper>.ant-input-number>.ant-input-number-input-wrap>.ant-input-number-input"
stock_input = "[placeholder=\"Stock\"]"
weight_input = "[placeholder=\"Weight\"]"
sku_input = "[placeholder=\"SKU\"]"
barcode_input = "[placeholder=\"Bar Code\"]"
apply_button = ".variantInfo___1m5bJ>.ant-btn.ant-btn-primary"
weight_text = "#weight"
sizeX_text = "#sizeX"
sizeY_text = "#sizeY"
sizeZ_text = "#sizeZ"
spu_text = "#spu"
addcategory_spn = ".addCategoriesBtn___1xYnW"




def adminCreateAdvanceProduct(page, productname, description, picname, price,
                       stock, attributename, variation0, option0, option1, option2,
                       option3, variation1, optiona, variation2, optionb, weight, sku,
                       barcode, sizeX, sizeY, sizeZ, spu, ):
    # Go to https://admin-tg-test.chunsutech.com/product/list
    page.goto(product_url)
    # Click button:has-text("Add Product")
    page.locator(create_button).click()
    # Fill text=Product Name0 / 120 >> [placeholder="请输入"]
    page.locator(productname_text).fill(productname)
    # Fill textarea
    page.locator(describe_text).fill(description)
    # Upload BananaClientCode.txt
    page.locator(pic_input).set_input_files(picname)
    ##
    page.wait_for_timeout(10000)

#   添加商品属性
    # Click button:has-text("添加商品属性")
    page.locator(button_attribute).click()
    # Click button:has-text("Add New Attributes")
    page.locator(button_add).click()
     # Fill text=NameType请选择 >> [placeholder="请输入"]
    page.locator(attributename_text).fill(attributename)
    # Click text=Type请选择 >> input[role="combobox"]
    page.locator(type_select).click()
    # Click .ant-select-item >> nth=0
    page.locator(type_label).click()
    # Click button:has-text("确 定")
    page.locator(submit_text).click()
    ##
    page.wait_for_timeout(10000)
    # Click [aria-label="reload"] svg
    page.locator(svg_span).click()
    # Fill [placeholder="选择属性项搜索，或者输入关键字识别搜索"]
    page.locator(attributename_search).fill(attributename)
    # Click text=Add New Attributes属性(集) >> button >> nth=1
    page.locator(svg_search).click()
    # Click [aria-label="reload"] svg
    page.locator(svg_span).click()
    # Check text=1Text0 >> input[type="checkbox"]
    page.locator(td_select).check()
     # Click button:has-text("Submit")
    page.locator(submit_attribute).click()

#   添加变体
    # Click button:has-text("Enable Variations")
    page.locator(variation_span).click()
    # Fill [placeholder="Enter Vairation Name\,eg\:colour\,etc\."]
    page.locator(variation0_text).fill(variation0)
    # Click button:has-text("Add Options")
    page.locator(addoption_button).click()
    page.locator(addoption_button).click()
    page.locator(addoption_button).click()
    # page.locator(pic_option)
    content = page.locator(pic_option)
    for testpic in content.element_handles():
        # print(f'\ncontent={testpic.get_attribute("id")}')
        page.set_input_files("#"+testpic.get_attribute("id"), pic_url)
    ##
    page.wait_for_timeout(10000)
    # Fill [placeholder="Enter Vairation Name\,eg\:Red\,etc\."] >> nth=0
    page.locator(option_text).first.fill(option0)
    # Fill [placeholder="Enter Vairation Name\,eg\:Red\,etc\."] >> nth=1
    page.locator(option_text).nth(1).fill(option1)
    # Fill [placeholder="Enter Vairation Name\,eg\:Red\,etc\."] >> nth=2
    page.locator(option_text).nth(2).fill(option2)
     # Fill [placeholder="Enter Vairation Name\,eg\:Red\,etc\."] >> nth=3
    page.locator(option_text).nth(3).fill(option3)
    # Click button:has-text("Add Variation")
    page.locator(addvariation_button).click()
    page.locator(addvariation_button).click()
    # Fill text=Variation1OptionsAdd Options >> [placeholder="Enter Vairation Name\,eg\:colour\,etc\."]
    page.locator(variation1_text).fill(variation1)
    # Fill text=Variation1OptionsAdd Options >> [placeholder="Enter Vairation Name\,eg\:Red\,etc\."]
    page.locator(optiona_text).fill(optiona)
     # Fill text=Variation2OptionsAdd Options >> [placeholder="Enter Vairation Name\,eg\:colour\,etc\."]
    page.locator(variation2_text).fill(variation2)
    # Fill text=Variation2OptionsAdd Options >> [placeholder="Enter Vairation Name\,eg\:Red\,etc\."]
    page.locator(optionb_text).fill(optionb)
    # Fill [placeholder="Price"]
    page.locator(price_input).fill(price)
    # Fill [placeholder="Stock"]
    page.locator(stock_input).fill(stock)
    # # Fill [placeholder="Weight"]
    # page.locator(weight_input).fill(weight)
    # Fill [placeholder="SKU"]
    page.locator(sku_input).fill(sku)
    # Fill [placeholder="Bar Code"]
    page.locator(barcode_input).fill(barcode)
    # Click button:has-text("Apply To All")
    page.locator(apply_button).click()
    # Fill text=重量Kg >> [placeholder="请输入"]
    page.locator(weight_text).fill(weight)
    # Fill text=尺寸cm >> [placeholder="请输入"]
    page.locator(sizeX_text).fill(sizeX)
    # Fill #sizeY
    page.locator(sizeY_text).fill(sizeY)
    # Fill #sizeZ
    page.locator(sizeZ_text).fill(sizeZ)
    # Fill #spu
    page.locator(spu_text).fill(spu)

#   添加Category
    # Click button:has-text("Add New Categories")
    page.locator(addcategory_spn).click()