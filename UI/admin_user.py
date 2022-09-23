user_url = "https://admin-tg-test.chunsutech.com/users/users"
createuser_button = ".ant-btn.ant-btn-primary"
username_text = "#username"
name_text = "#name"
email_text = "#email"
role_select = ".ant-select-selection-overflow"
role_listbox = "role_ids_list"
password_text = "#password"
confirm_button = ".ant-space-item>.ant-btn.ant-btn-primary"



def createUser(page, username, fullname, email, password):
    # Go to https://admin-tg-dev.chunsutech.com/users/users
    page.goto(user_url)
    # Click button:has-text("Create User")
    page.locator(createuser_button).click()
    # Fill [placeholder="\35 -15 alphabets or numbers"]
    page.locator(username_text).fill(username)
    # Fill text=Fullname0 / 32 >> [placeholder="请输入"]
    page.locator(name_text).fill(fullname)
    # Fill #email
    page.locator(email_text).fill(email)
    # Click .ant-select-selector
    page.locator(role_select).click()
    # Click div:nth-child(5) > .ant-row > div >> nth=0
    page.locator(role_listbox).click()
    # Fill input[type="password"]
    page.locator(password_text).fill(password)
    # Click button:has-text("确 定")
    page.locator(confirm_button).click()

search_text = ".ant-input-wrapper"
search_button = ".ant-btn.ant-btn-default.ant-btn-icon-only.ant-input-search-button"
refresh_svg = ".anticon.anticon-reload"

def searchUser(page, searchdata):
    # Go to https://admin-tg-dev.chunsutech.com/users/users
    page.goto(user_url)
    # Fill [placeholder="commodity\.list\.search\.placeholder"]
    page.locator(search_text).fill(searchdata)
    # Click button >> nth=1
    page.locator(search_button).click()
    # Click [aria-label="reload"] svg
    page.locator(refresh_svg).click()
