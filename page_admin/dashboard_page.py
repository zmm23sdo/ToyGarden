from base.base_page import BasePage

class DashboardPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page