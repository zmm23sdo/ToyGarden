from base.base_page import BasePage

class MediaPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    media_url = "https://admin-tg-test.chunsutech.com/system/media"