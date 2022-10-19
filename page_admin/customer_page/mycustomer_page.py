from base.base_page import BasePage

class CustomerPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    customer_url = "https://admin-tg-test.chunsutech.com/customer/list"

    def AddCustomer(self, customername, phone, email, firstname, lastname, age, remark):
        # Go to https://admin-tg-test.chunsutech.com/customer/list
        self.visit(self.customer_url)
        # Click button:has-text("Add Customer")
        self.click("button:has-text(\"Add Customer\")")
         # Fill #customerName
        self.fill("#customerName", customername)
         # Fill text=Phone Number+ 60 >> [placeholder="请输入"]
        self.fill("#phoneNumber", phone)
        # Fill #email
        self.fill("#email", email)
        # Fill #firstName
        self.fill("#firstName", firstname)
        # Fill #lastName
        self.fill("#lastName", lastname)
        # Click text=Gender请选择 >> input[role="combobox"]
        self.click("#gender")
        # Click text=male >> nth=1
        self.click(".ant-select-item.ant-select-item-option.ant-pro-filed-search-select-option.ant-select-item-option-active.ant-select-item-option-selected")
        # Fill text=GendermaleAge >> [placeholder="请输入"]
        self.fill("#age", age)
        # Fill textarea
        self.fill("#remarks", remark)
        # Click button:has-text("Submit")
        self.click("button:has-text(\"Submit\")")

    def SearchCustomer(self, search_data):
        # Go to https://admin-tg-test.chunsutech.com/customer/list
        self.visit(self.customer_url)
        # Fill text=Add CustomerIDCustomer NameNamePhone NumberEmailTypeStateOperation暂无数据 >> [placeholder="请输入"]
        self.fill("#search", search_data)
        ##########################
        # Click button >> nth=1
        self.click(".ant-input-group-addon")
        # Click [aria-label="reload"] svg
        self.click(".anticon.anticon-reload")
        ##########################
        