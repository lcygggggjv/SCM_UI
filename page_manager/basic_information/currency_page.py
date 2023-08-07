import time

from common.mock import Mock
from page_manager.basepage import BasePage


class CurrencyPage(BasePage):

    mock = Mock()

    def create_currency(self):
        """新增币种"""

        time.sleep(1)
        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增币种']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('88888')
        elif self.is_el_present(('xpath', "//td[text()='99999'][@label='币种编码']")):
            self.driver.find_element("xpath", "//button[text()='新增币种']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]')\
                .send_keys(self.mock.faker_pystr())
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')\
                .send_keys(self.mock.faker_pystr())
        else:
            self.driver.find_element("xpath", "//button[text()='新增币种']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('88888')
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_currency_required(self):
        """新增币种必填"""

        self.driver.find_element("xpath", "//button[text()='新增币种']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_currency_code_length(self):
        """新增币种编码长度校验"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(self.mock.mock_data())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入5个字以内的内容']"))
        return assert_info

    def create_currency_name_length(self):
        """新增币种名称长度校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def create_currency_code_uniqueness(self):
        """新增单位名称唯一性"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
        assert_info = self.get_alert(("xpath", "//div[text()='该币种编码已存在，请重新输入']"))
        return assert_info

    def create_currency_two(self):
        """新增币种2"""

        time.sleep(1)
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(
            self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_currency_three(self):
        """新增币种3"""

        time.sleep(1)
        self.driver.find_element("xpath", "//button[text()='新增币种']").click()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]') \
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]') \
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def setting_default_currency(self):
        """设置默认币种"""

        time.sleep(1.5)
        self.driver.find_element("xpath", "//button[text()='设置默认币种']").click()
        self.driver.find_element("xpath", '//input[@autocomplete="off"]').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='设置默认币种成功']"))
        return assert_info

    def update_currency(self):
        """编辑币种"""

        time.sleep(1.8)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='编辑成功']"))
        return assert_info

    def update_currency_required(self):
        """编辑币种名称必填"""

        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def update_currency_length(self):
        """编辑币种名称，长度校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def update_currency_code_disable(self):
        """编辑币种编码，置灰属性"""

        el = self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]')
        assert_info = el.get_attribute("disabled")
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def search_currency_code(self):
        """精确搜索币种编码"""

        self.driver.find_element('xpath', '//input[@name="no"]').send_keys('99999')
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='99999'][@label='币种编码']"))
        return assert_info

    def currency_resetting_search(self):
        """重置搜索"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        el = self.driver.find_element('xpath', '//input[@name="no"]')
        assert_info = el.get_attribute('value')
        return assert_info

    def search_currency_name(self):
        """精确搜索币种名称"""

        time.sleep(1.5)
        self.driver.find_element('xpath', '//input[@name="name"]').send_keys('88888')
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='88888'][@label='币种名称']"))
        return assert_info

    def delete_currency(self):
        """删除币种"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        self.driver.find_element("xpath", '(//span[@aria-label="删除"])[1]').click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info

    def batch_delete_currency(self):
        """批量删除币种"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//input[@type="checkbox"])[2]').click()
        self.driver.find_element("xpath", "//button[text()='删除']").click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info
