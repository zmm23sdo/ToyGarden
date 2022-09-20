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


def adminCreateBasicProduct(page, productname, description, picname, price,
                       stock, transPrice):
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
