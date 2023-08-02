import time

from common.mock import Mock
from page_manager.basepage import BasePage


class ReasonPage(BasePage):

    mock = Mock()

    def create_reason(self):
        """新增原因"""

        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增原因']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]').send_keys('88888')

        elif self.is_el_present(('xpath', "//td[text()='99999'][@label='原因编码']")):
            self.driver.find_element("xpath", "//button[text()='新增原因']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]')\
                .send_keys(self.mock.faker_pystr())
            self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]')\
                .send_keys(self.mock.faker_pystr())

        else:
            self.driver.find_element("xpath", "//button[text()='新增原因']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]').send_keys('88888')

        self.driver.find_element("xpath", '//input[@role="combobox"][@placeholder="请选择"]').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_reason_required(self):
        """新增原因必填"""

        self.driver.find_element("xpath", "//button[text()='新增原因']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_reason_code_length(self):
        """新增原因编码长度校验"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(self.mock.mock_data())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入5个字以内的内容']"))
        return assert_info

    def create_reason_name_length(self):
        """新增原因名称长度校验"""

        self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        return assert_info

    def create_reason_code_uniqueness(self):
        """新增原因编码唯一性"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
        assert_info = self.get_alert(("xpath", "//div[text()='该原因编码已存在，请重新输入']"))
        return assert_info

    def create_reason_two(self):
        """新增原因2"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]').send_keys(
            self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@role="combobox"][@placeholder="请选择"]').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def update_reason(self):
        """编辑原因"""

        time.sleep(1.8)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='编辑成功']"))
        return assert_info

    def update_reason_required(self):
        """编辑原因名称必填"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]').clear()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def update_reason_code_type_disable(self):
        """编辑原因编码，原因类型，置灰属性"""

        el_list = ['//input[@name="no"][@placeholder="请输入"]', '//input[@role="combobox"][@aria-autocomplete="both"]']

        for xpath in el_list:

            el = self.driver.find_element("xpath", xpath)
            if not el.get_attribute('disabled'):
                return False
        return True

    def update_reason_name_length(self):
        """编辑原因名称，长度校验"""

        self.driver.find_element("xpath", '//input[@name="explain"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", '//button[text()="取消"]').click()
        return assert_info

    def search_reason_code(self):
        """精确搜索原因编码"""

        self.driver.find_element('xpath', '//input[@name="no"]').send_keys('99999')
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='99999'][@label='原因编码']"))
        return assert_info

    def resetting_search(self):
        """重置搜索"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        el = self.driver.find_element('xpath', '//input[@name="no"]')
        assert_info = el.get_attribute('value')
        return assert_info

    def search_reason_name(self):
        """精确搜索原因名称"""

        time.sleep(1.5)
        self.driver.find_element('xpath', '//input[@name="explain"]').send_keys('88888')
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='88888'][@label='原因描述']"))
        return assert_info

    def search_reason_type(self):
        """精确搜索原因类型"""

        self.driver.find_element('xpath', '//input[@role="combobox"][@aria-autocomplete="list"]').click()
        self.driver.find_element('xpath', '//li[@data-option-index="0"]').click()
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='取消'][@label='原因类型']"))
        return assert_info

    def delete_reason(self):
        """删除原因"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        self.driver.find_element("xpath", '(//span[@aria-label="删除"])[1]').click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info

    def batch_delete_reason(self):
        """批量删除原因"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="勾选当页"])[1]').click()
        self.driver.find_element("xpath", "//button[text()='删除']").click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info
