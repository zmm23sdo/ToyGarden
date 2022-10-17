from base.base_page import BasePage

class CategoriesPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    categories_url = "https://admin-tg-test.chunsutech.com/product/categories"
    add_root_button = "button:has-text(\"Add Root Category\")"
    category_name_text = "#name"
    submit_button = ".ant-space.ant-space-horizontal.ant-space-align-center.actions___1hlEJ>.ant-space-item>.ant-btn.ant-btn-primary"
    bubble_button = ".ant-message-notice-content"

    def CreateRootCategory(self, category_name):
        # Go to https://admin-tg-test.chunsutech.com/product/categories/
        self.visit(self.categories_url)
        # Click button:has-text("Add Root Category")
        self.click(self.add_root_button)
        # Fill text=Category NameEnable CategoryInclude in MenuProducts MerchandisingSPUAdd Products >> [placeholder="请输入"]
        self.fill(self.category_name_text, category_name)
        # Click button:has-text("Submit")
        self.click(self.submit_button)
        # Click .ant-message-notice-content
        self.click(self.bubble_button)


    first_category = ":nth-child(1) > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal"
    edit_button = submit_button
    save_button = edit_button

    def EditCategory(self, new_category_name):
        # Go to https://admin-tg-test.chunsutech.com/product/categories/
        self.visit(self.categories_url)
        # Click span:has-text("123") >> nth=0
        self.click(self.first_category)
        # Click button:has-text("Edit")
        self.click(self.edit_button)
        # Fill text=Category NameEnable CategoryInclude in MenuProducts MerchandisingSPUAdd Products >> [placeholder="请输入"]
        self.fill(self.category_name_text, new_category_name)
        # Click button:has-text("Save")
        self.click(self.save_button)
        # Click .ant-message-notice-content
        self.click(self.bubble_button)

    add_sub_button = "button:has-text(\"Add Subcategory\")"

    def CreateSubcategory(self, ):
        # Go to https://admin-tg-test.chunsutech.com/product/categories/
        self.visit(self.categories_url)
        # Click span:has-text("123") >> nth=0
        self.click(self.first_category)
        # Click button:has-text("Add Subcategory")
        self.click(self.add_sub_button)


