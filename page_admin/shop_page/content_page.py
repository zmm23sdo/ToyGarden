from base.base_page import BasePage

class ContentDecorationPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    content_url = "https://admin-tg-test.chunsutech.com/shop/content"