import time
from common.mock import Mock
from page_manager.basepage import BasePage


class TaxRatePage(BasePage):
    """税率数值输入框，需要使用双击删除或者键盘操作，control/command+ a"""

    mock = Mock()

    def create_tax_rate(self):
        """新增税率"""

        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增税率']").click()
            self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(9)
        elif self.is_el_present(('xpath', "//td[text()='9'][@label='税率（%）']")):
            self.driver.find_element("xpath", "//button[text()='新增税率']").click()
            self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(self.mock.random_int())
        else:
            self.driver.find_element("xpath", "//button[text()='新增税率']").click()
            self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(9)
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_tax_rate_required(self):
        """新增税率必填"""

        self.driver.find_element("xpath", "//button[text()='新增税率']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_tax_negative_num(self):
        """新增税率 负数校验"""

        self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(-1)
        assert_info = self.get_alert(("xpath", "//div[text()='请输入0~99的整数']"))
        return assert_info

    def create_tax_most_num(self):
        """新增税率超过100校验 """

        self.double_click_delete('//input[@name="rate"]')
        # self.driver.find_element("xpath", '//input[@name="rate"]').clear()
        self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(101)
        assert_info = self.get_alert(("xpath", "//div[text()='请输入0~99的整数']"))
        return assert_info

    def create_tax_str(self):
        """新增税率 输入字符串等校验"""

        self.double_click_delete('//input[@name="rate"]')
        self.driver.find_element("xpath", '//input[@name="rate"]').send_keys('xx')
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_tax_float(self):
        """新增税率 小数等校验"""

        self.double_click_delete('//input[@name="rate"]')
        self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(1.53)
        assert_info = self.get_alert(("xpath", "//div[text()='请输入0~99的整数']"))
        return assert_info

    def create_tax_uniqueness(self):
        """新增税率 唯一性"""

        self.double_click_delete('//input[@name="rate"]')
        self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(9)
        assert_info = self.get_alert(("xpath", "//div[text()='该税率已存在，请重新输入']"))
        return assert_info

    def create_tax_rate_two(self):
        """新增税率2"""

        self.double_click_delete('//input[@name="rate"]')
        self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(self.mock.random_int())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def open_checkbox(self):
        """打开税率开关"""

        time.sleep(1.8)
        self.driver.find_element("xpath", '(//td[@label="是否生效"]//span)[1]').click()
        self.driver.find_element("xpath", '//button[text()="生效"]').click()
        assert_info = self.get_alert(("xpath", "//div[text()='生效成功']"))
        return assert_info

    def search_tax_rate(self):
        """精确搜索税率"""

        self.driver.find_element('xpath', '//input[@name="search"]').send_keys(9)
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='9'][@label='税率（%）']"))
        return assert_info

    def resetting_search(self):
        """重置搜索"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        el = self.driver.find_element('xpath', '//input[@name="search"]')
        assert_info = el.get_attribute('value')
        return assert_info

    def delete_tax_rate(self):
        """删除税率"""

        self.driver.find_element("xpath", '(//span[@aria-label="删除"])[1]').click()
        self.driver.find_element("xpath", "//button[text()='删除']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info
