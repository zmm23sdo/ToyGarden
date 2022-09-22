customer_url = "https://admin-tg-test.chunsutech.com/customer/list"
create_customer_url = "https://admin-tg-test.chunsutech.com/customer/create"
addcustomer_button = ".ant-btn.ant-btn-primary"

def addCustomer(page):
    # Go to https://admin-tg-test.chunsutech.com/customer/list/
    page.goto("https://admin-tg-test.chunsutech.com/customer/list/")
    # Click button:has-text("Add Customer")
    page.locator(addcustomer_button).click()
    page.wait_for_url(create_customer_url)


def searchCustomer(page):
    # Go to https://admin-tg-test.chunsutech.com/customer/list
    page.goto("https://admin-tg-test.chunsutech.com/customer/list")
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill("test")
    # Press Enter
    page.locator("[placeholder=\"请输入\"]").press("Enter")
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
