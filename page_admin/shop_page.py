from base.base_page import BasePage

class ShopPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    shop_address_url = "https://admin-tg-test.chunsutech.com/shop/address"
    shop_decoration_url = "https://admin-tg-test.chunsutech.com/shop/decoration"
    create_address_button = "button:has-text(\"Add Address\")"
    phoneNumber_text = "#phoneNumber"
    firstName_text = "#firstName"
    lastName_text = "#lastName"
    company_text = "#company"
    street_text = "#street"
    city_text = "#city"
    state_selector = "#state"
    state_option = ".ant-select-item-option-selected"
    postcode_text = "#postcode"
    country_selector = "#country"
    country_list_0 = "#country_list_0"
    check_input = "input[type=\"checkbox\"]"
    confirm_button = "button:has-text(\"确 定\")"

    def CreateAddress(self, phoneNumber, firstName, lastName, company, street, city,
                            postcode):
        # Go to https://admin-tg-test.chunsutech.com/shop/address
        self.visit(self.shop_address_url)
        # Click button:has-text("Add Address")
        self.click(self.create_address_button)
        # Fill text=Phone Number+ 60 >> [placeholder="请输入"]
        self.fill(self.phoneNumber_text, phoneNumber)
        # Fill #firstName
        self.fill(self.firstName_text, firstName)
        # Fill #lastName
        self.fill(self.lastName_text, lastName)
        # Fill #company
        self.fill(self.company_text, company)
        # Fill textarea
        self.fill(self.street_text, street)
        # Fill #city
        self.fill(self.city_text, city)
        # Click text=State请选择 >> input[role="combobox"]
        self.click(self.state_selector)
        # Click .ant-select-item >> nth=0
        self.click(self.state_option)
        # Fill #postcode
        self.fill(self.postcode_text, postcode)
        # Click text=Country请选择 >> input[role="combobox"]
        self.click(self.country_selector)
        # Click text=Malaysia
        self.click(self.country_list_0)
        # Check input[type="checkbox"] >> nth=0
        self.locator(self.check_input).first.check()
        # Check input[type="checkbox"] >> nth=1
        self.locator(self.check_input).nth(1).check()
        # Click button:has-text("确 定")
        self.click(self.confirm_button)

    edit_address_button = "button:has-text(\"Edit\")"

    def EditAddress(self, new_phoneNumber, new_firstName, new_lastName, new_company, new_street, new_city,
                            new_postcode):
        # Go to https://admin-tg-test.chunsutech.com/shop/address
        self.visit(self.shop_address_url)
        # Click button:has-text("Edit") >> nth=0
        self.locator(self.edit_address_button).first.click()
        self.fill(self.phoneNumber_text, new_phoneNumber)
        # Fill #firstName
        self.fill(self.firstName_text, new_firstName)
        # Fill #lastName
        self.fill(self.lastName_text, new_lastName)
        # Fill #company
        self.fill(self.company_text, new_company)
        # Fill textarea
        self.fill(self.street_text, new_street)
        # Fill #city
        self.fill(self.city_text, new_city)
        # Click text=State请选择 >> input[role="combobox"]
        self.click(self.state_selector)
        # Click .ant-select-item >> nth=0
        self.click(self.state_option)
        # Fill #postcode
        self.fill(self.postcode_text, new_postcode)
        # Click text=Country请选择 >> input[role="combobox"]
        self.click(self.country_selector)
        # Click text=Malaysia
        self.click(self.country_list_0)
        # Check input[type="checkbox"] >> nth=0
        self.locator(self.check_input).first.check()
        # Check input[type="checkbox"] >> nth=1
        self.locator(self.check_input).nth(1).check()
        # Click button:has-text("确 定")
        self.click(self.confirm_button)

    delete_address_button = "button:has-text(\"Delete\")"
    delete_confirm_button= "button:has-text(\"Confirm\")"

    def DeleteAddress(self):
        # Go to https://admin-tg-test.chunsutech.com/shop/address
        self.visit(self.shop_address_url)
        # Click button:has-text("Delete") >> nth=0
        self.locator(self.delete_address_button).first.click()
        # Click button:has-text("Confirm")
        self.click(self.delete_confirm_button)

    # carouse_

    def DecorationCarousel(self, ):
        # Go to https://admin-tg-test.chunsutech.com/shop/decoration/
        self.visit(self.shop_address_url)
        # Click text=carousel
        # page.locator("text=carousel").click()






