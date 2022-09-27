from playwright.sync_api import sync_playwright

class BasePage:

    browser = sync_playwright().start().chromium.launch(headless=False)

    def open(self):
        self.page = self.browser.new_page()
    # 访问URL
    def visit(self, url):
        self.page.goto(url)
    # 元素定位
    def locator(self, loc):
        return self.page.locator(loc)
    # 输入
    def input(self, loc, txt):
        self.locator(loc).set_input_files(txt)
    # text键入
    def fill(self, loc, txt):
        self.locator(loc).fill(txt)
    # 点击
    def click(self, loc):
        self.locator(loc).click()
    # # 定位文案
    # def content(self, loc):
    #     self.page.text_content(loc)
    # 等待
    def wait(self, time):
       self.page.wait_for_timeout(time)

    # 关闭
    def close(self):
        self.page.close()

