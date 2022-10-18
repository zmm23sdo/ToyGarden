from base.base_page import BasePage

class ShopAddressPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    shop_address_url = "https://admin-tg-test.chunsutech.com/shop/address"
    shop_decoration_url = "https://admin-tg-test.chunsutech.com/shop/decoration"
    # create_address_button = "button:has-text(\"Add Address\")"
    # phoneNumber_text = "#phoneNumber"
    # firstName_text = "#firstName"
    # lastName_text = "#lastName"
    # company_text = "#company"
    # street_text = "#street"
    # city_text = "#city"
    # state_selector = "#state"
    # state_option = ".ant-select-item-option-selected"
    # postcode_text = "#postcode"
    # country_selector = "#country"
    # country_list_0 = "#country_list_0"
    # check_input = "input[type=\"checkbox\"]"
    # confirm_button = "button:has-text(\"确 定\")"

    def CreateAddress(self, phoneNumber, firstName, lastName, company, street, city,
                            postcode):
        # Go to https://admin-tg-test.chunsutech.com/shop/address
        self.visit(self.shop_address_url)
        # Click button:has-text("Add Address")
        self.click("button:has-text(\"Add Address\")")
        # Fill text=Phone Number+ 60 >> [placeholder="请输入"]
        self.fill("#phoneNumber", phoneNumber)
        # Fill #firstName
        self.fill("#firstName", firstName)
        # Fill #lastName
        self.fill("#lastName", lastName)
        # Fill #company
        self.fill("#company", company)
        # Fill textarea
        self.fill("#street", street)
        # Fill #city
        self.fill("#city", city)
        # Click text=State请选择 >> input[role="combobox"]
        self.click("#state")
        # Click .ant-select-item >> nth=0
        self.click(".ant-select-item-option-selected")
        # Fill #postcode
        self.fill("#postcode", postcode)
        # Click text=Country请选择 >> input[role="combobox"]
        self.click("#country")
        # Click text=Malaysia
        self.click("#country_list_0")
        # Check input[type="checkbox"] >> nth=0
        self.locator("input[type=\"checkbox\"]").first.check()
        # Check input[type="checkbox"] >> nth=1
        self.locator("input[type=\"checkbox\"]").nth(1).check()
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")#   Confirm

    # edit_address_button = "button:has-text(\"Edit\")"

    def EditAddress(self, new_phoneNumber, new_firstName, new_lastName, new_company, new_street, new_city,
                            new_postcode):
        # Go to https://admin-tg-test.chunsutech.com/shop/address
        self.visit(self.shop_address_url)
        # Click button:has-text("Edit") >> nth=0
        self.locator("button:has-text(\"Edit\")").first.click()
        self.fill("#phoneNumber", new_phoneNumber)
        # Fill #firstName
        self.fill("#firstName", new_firstName)
        # Fill #lastName
        self.fill("#lastName", new_lastName)
        # Fill #company
        self.fill("#company", new_company)
        # Fill textarea
        self.fill("#street", new_street)
        # Fill #city
        self.fill("#city", new_city)
        # Click text=State请选择 >> input[role="combobox"]
        self.click("#state")
        # Click .ant-select-item >> nth=0
        self.click(".ant-select-item-option-selected")
        # Fill #postcode
        self.fill("#postcode", new_postcode)
        # Click text=Country请选择 >> input[role="combobox"]
        self.click("#country")
        # Click text=Malaysia
        self.click("#country_list_0")
        # Check input[type="checkbox"] >> nth=0
        self.locator("input[type=\"checkbox\"]").first.check()
        # Check input[type="checkbox"] >> nth=1
        self.locator("input[type=\"checkbox\"]").nth(1).check()
        # Click button:has-text("确 定")
        self.click("button:has-text(\"确 定\")")

    # delete_address_button = "button:has-text(\"Delete\")"
    # delete_confirm_button= "button:has-text(\"Confirm\")"

    def DeleteAddress(self):
        # Go to https://admin-tg-test.chunsutech.com/shop/address
        self.visit(self.shop_address_url)
        # Click button:has-text("Delete") >> nth=0
        self.locator("button:has-text(\"Delete\")").first.click()
        # Click button:has-text("Confirm")
        self.click("button:has-text(\"Confirm\")")