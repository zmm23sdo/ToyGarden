home_url = "https://client-tg-test.chunsutech.com/"

account_button = "button:has-text(\"Account\")"




def client_signin(page):
    # Go to https://client-tg-test.chunsutech.com/
    page.goto(home_url)
    # Click button:has-text("Account")
    page.locator(account_button).click()