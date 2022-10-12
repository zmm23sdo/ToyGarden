from base.base_page import BasePage

class LoginPage(BasePage):

    client_url = "https://client-tg-test.chunsutech.com/"
    signin_url = "https://client-tg-test.chunsutech.com/customer/account/login"

    def __init__(self) -> None:
        super().__init__()
        self.open()

    account_button = "button:has-text(\"Account\")"
    signin_select = "text=Sign In"
    signin_button = ".flex.items-center.justify-center.gap-2"
    phone_tip = "text=PhoneThis is a required field. >> div"
    vcode_tip = "text=This is a required field."

    def signin_empty(self):
        # Go to https://client-tg-test.chunsutech.com/
        self.visit(self.client_url)
        # Click button:has-text("Account")
        self.click(self.account_button)
        # Click text=Sign In >> nth=3
        self.locator(self.signin_select).nth(3).click()
        self.page.wait_for_url(self.signin_url)
        
        # Click main button:has-text("Sign In")
        self.click(self.signin_button)
        # Click text=PhoneThis is a required field. >> div
        self.click(self.phone_tip)
        tip_phone = self.page.text_content(self.phone_tip)
        # Click text=This is a required field. >> nth=1
        self.locator(self.vcode_tip).nth(1).click()
        tip_vcode = self.page.text_content(self.vcode_tip)
        return tip_phone, tip_vcode

    vcode_text = "#vcode"

    def signin_phone_empty(self, vcode):
        # Go to https://client-tg-test.chunsutech.com/
        self.visit(self.client_url)
        # Click button:has-text("Account")
        self.click(self.account_button)
        # Click text=Sign In >> nth=3
        self.locator(self.signin_select).nth(3).click()
        self.page.wait_for_url(self.signin_url)

        # Fill text=VcodeGET >> input[type="text"]
        self.fill(self.vcode_text, vcode)
        # Click main button:has-text("Sign In")
        self.click(self.signin_button)
        # Click text=PhoneThis is a required field. >> div
        self.click(self.phone_tip)
        tip = self.page.text_content(self.phone_tip)
        return tip

    phone_text = "#phone"

    def signin_vcode_empty(self, phone):
        # Go to https://client-tg-test.chunsutech.com/
        self.visit(self.client_url)
        # Click button:has-text("Account")
        self.click(self.account_button)
        # Click text=Sign In >> nth=3
        self.locator(self.signin_select).nth(3).click()
        self.page.wait_for_url(self.signin_url)
        # Fill text=PhonePlease fill in valid phone number. >> input[type="text"]
        self.fill(self.phone_text, phone)
        # Click main button:has-text("Sign In")
        self.click(self.signin_button)
        # Click text=This is a required field. >> nth=1
        self.locator(self.vcode_tip).nth(1).click()
        tip = self.page.text_content(self.vcode_tip)
        return tip
    
    phone_err_tip = "text=Please fill in valid phone number."

    def signin_phone_valid(self, phone, vcode):
        # Go to https://client-tg-test.chunsutech.com/
        self.visit(self.client_url)
        # Click button:has-text("Account")
        self.click(self.account_button)
        # Click text=Sign In >> nth=3
        self.locator(self.signin_select).nth(3).click()
        self.page.wait_for_url(self.signin_url)
        # Fill text=PhonePlease fill in valid phone number. >> input[type="text"]
        self.fill(self.phone_text, phone)
        # Fill text=VcodeGET >> input[type="text"]
        self.fill(self.vcode_text, vcode)
        # Click main button:has-text("Sign In")
        self.click(self.signin_button)
        # Click text=PhoneThis is a required field. >> div
        self.click(self.phone_err_tip)
        tip = self.page.text_content(self.phone_err_tip)
        return tip

    vcode_err_tip = "text=Phone number error"

    def sigin_phone_error(self, phone, vcode):
        # Go to https://client-tg-test.chunsutech.com/
        self.visit(self.client_url)
        # Click button:has-text("Account")
        self.click(self.account_button)
        # Click text=Sign In >> nth=3
        self.locator(self.signin_select).nth(3).click()
        self.page.wait_for_url(self.signin_url)
        # Fill text=PhonePlease fill in valid phone number. >> input[type="text"]
        self.fill(self.phone_text, phone)
        # Fill text=VcodeGET >> input[type="text"]
        self.fill(self.vcode_text, vcode)
        # Click main button:has-text("Sign In")
        self.click(self.signin_button)
        # Click text=PhoneThis is a required field. >> div
        self.click(self.vcode_err_tip)
        tip = self.page.text_content(self.vcode_err_tip)
        return tip

    get_button = "text=GET"

    def signin_getvcode_phone_error(self, phone):
        # Go to https://client-tg-test.chunsutech.com/
        self.visit(self.client_url)
        # Click button:has-text("Account")
        self.click(self.account_button)
        # Click text=Sign In >> nth=3
        self.locator(self.signin_select).nth(3).click()
        self.page.wait_for_url(self.signin_url)
        # Fill text=PhonePlease fill in valid phone number. >> input[type="text"]
        self.fill(self.phone_text, phone)
        # Click text=GET
        self.click(self.get_button)
        # Click text=PhoneThis is a required field. >> div
        self.click(self.vcode_err_tip)
        tip = self.page.text_content(self.vcode_err_tip)
        return tip

    def signin_password_empty(self, phone):




