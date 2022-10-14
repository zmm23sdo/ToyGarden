from base.base_page import BasePage

class CategoriesPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    categories_url = "https://admin-tg-test.chunsutech.com/product/categories"
    add_root_button = "button:has-text(\"Add Root Category\")"

    def CreateRootCategory(self):
        # Go to https://admin-tg-test.chunsutech.com/product/categories/
        self.visit(self.categories_url)
        # Click button:has-text("Add Root Category")
        self.click(self.add_root_button)

    first_category = ":nth-child(1) > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal"

    def EditCategory(self, ):
        # Go to https://admin-tg-test.chunsutech.com/product/categories/
        self.visit(self.categories_url)
        # Click span:has-text("123") >> nth=0
        self.click(self.first_category)
        