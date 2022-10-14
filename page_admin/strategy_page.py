from base.base_page import BasePage

class StrategyPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    strategy_url = "https://admin-tg-test.chunsutech.com/setting/strategy"
    create_button = ".ant-btn.ant-btn-primary.topBtn___24R_L"
    strategyname_text = "#name"
    direction_selector = "#direction"
    direction_list = "#direction_list"
    resolve_method = "#resolve_method"
    resolve_method_list = "#resolve_method_list"
    outlet_system_x = "#outlet_system_x"
    outlet_system_x_list = "#outlet_system_x_list"
    comnfirm_button = "button:has-text(\"确 定\")"

    def CreateStrategy(self, strategyname):
        # Go to https://admin-tg-test.chunsutech.com/setting/strategy
        self.visit(self.strategy_url)
        # Click button:has-text("Add Strategy")
        self.click(self.create_button)
        # Fill [placeholder="请输入"]
        self.fill(self.strategyname_text, strategyname)
        # Click text=同步机制请选择 >> input[role="combobox"]
        self.click(self.direction_selector)
        # Click div[role="listbox"]:has-text("暂无数据")
        self.click(self.direction_list)
        # Click text=请选择Please select system >> input[role="combobox"]
        self.click(self.resolve_method)
         # Click div:nth-child(9) > div > .ant-select-dropdown
        self.click(self.resolve_method_list)
        # Click text=Xilnex指定门店请选择 >> input[role="combobox"]
        self.click(self.outlet_system_x)
        # Click #outlet_system_x_list
        self.click(self.outlet_system_x_list)
        # Click button:has-text("确 定") >> nth=0
        self.locator(self.comnfirm_button).first.click()



