product_url = "https://admin-tg-dev.chunsutech.com/product/list"
create_button = ".ant-btn.ant-btn-primary"
productname_text = "#name"
describe_text = "#describe"
pic_input = "#pic"
price_text = "#price"
stock_text = "#stock"
weight_text = "#weight"
sizeX_text = "sizeX"




def adminCreateBasicProduct(page, productname, description, picname, price,
                       stock, weight):
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
    # Fill text=价格RM >> [placeholder="请输入"]
    page.locator(price_text).fill(price)
    # Fill #stock
    page.locator(stock_text).fill(stock)
    # Fill text=重量Kg >> [placeholder="请输入"]
    page.locator(weight_text).fill(weight)
