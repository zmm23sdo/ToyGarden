product_url = "https://admin-tg-dev.chunsutech.com/product/list"
create_button = ".ant-btn.ant-btn-primary"
productname_text = "#name"
describe_text = "#describe"
pic_input = "#pic"
price_text = "#price"
stock_text = "#stock"
weight_text = "#weight"
sizeX_text = "#sizeX"
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

def adminCreateAdvanceProduct(page, productname, description, picname, price,
                       stock, attributename):
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
    
    # Fill text=价格RM >> [placeholder="请输入"]
    page.locator(price_text).fill(price)
    # Fill #stock
    page.locator(stock_text).fill(stock)