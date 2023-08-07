import time

from common.mock import Mock
from page_manager.basepage import BasePage


class MaterialSignalPage(BasePage):

    def create_signal(self):
        """新增物料信号"""

        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增物料信号']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('88888')

        elif self.is_el_present(('xpath', "//td[text()='99999'][@label='信号编码']")):
            self.driver.find_element("xpath", "//button[text()='新增物料信号']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(
                Mock.faker_pystr())
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(
                Mock.faker_pystr())

        else:
            self.driver.find_element("xpath", "//button[text()='新增物料信号']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('88888')

        self.driver.find_element("xpath", '//input[@name="srmUsageStatus"][@value="NORMAL"]').click()
        self.driver.find_element("xpath", '//input[@name="wmsUsageStatus"][@value="NORMAL"]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_signal_required(self):
        """新增信号必填"""

        self.driver.find_element("xpath", "//button[text()='新增物料信号']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_signal_code_length(self):
        """新增信号编码长度校验"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(Mock.mock_data())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入5个字以内的内容']"))
        return assert_info

    def create_signal_name_length(self):
        """新增信号名称长度校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(
            Mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def create_signal_uniqueness(self):
        """新增信号名称唯一性"""
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
        assert_info = self.get_alert(("xpath", "//div[text()='该信号编码已存在，请重新输入']"))
        return assert_info

    def create_signal_two(self):
        """新增信号2"""

        time.sleep(1)
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_signal_three(self):
        """新增信号3"""

        time.sleep(1.3)
        self.driver.find_element("xpath", "//button[text()='新增物料信号']").click()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def update_signal(self):
        """编辑物料信号"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element('xpath', '//input[@name="srmUsageStatus"][@value="WARNING"]').click()
        self.driver.find_element('xpath', '//input[@name="wmsUsageStatus"][@value="WARNING"]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='编辑成功']"))
        return assert_info

    def update_signal_required(self):
        """编辑物料必填"""

        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def update_signal_name_length(self):
        """编辑物料信号名称长度校验"""

        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(
            Mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def update_signal_disable(self):
        """编辑物料信号编码置灰属性"""

        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        el = self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]')
        assert_info = el.get_attribute("disabled")
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def search_signal_code(self):
        """精确搜索信号编码"""

        self.get_element(('xpath', '//input[@name="no"]')).send_keys('99999')
        self.get_element(('xpath', '//button[@aria-label="查询"]')).click()
        assert_info = self.get_alert(('xpath', "//td[text()='99999'][@label='信号编码']"))
        return assert_info

    def signal_resetting_search(self):
        """重置搜索"""

        self.get_element(("xpath", '//button[@aria-label="重置"]')).click()
        el = self.driver.find_element('xpath', '//input[@name="no"]')
        assert_info = el.get_attribute('value')
        return assert_info

    def search_signal_name(self):
        """精确搜索信号描述"""

        time.sleep(1.5)
        self.get_element(('xpath', '//input[@name="name"]')).send_keys('88888')
        self.get_element(('xpath', '//button[@aria-label="查询"]')).click()
        assert_info = self.get_alert(('xpath', "//td[text()='88888'][@label='信号描述']"))
        return assert_info

    def delete_signal(self):
        """删除物料信号"""

        # time.sleep(1.5)
        self.get_element(("xpath", '//button[@aria-label="重置"]')).click()
        self.driver.find_element("xpath", '(//span[@aria-label="删除"])[1]').click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info

    def batch_delete_signal(self):
        """批量删除物料信号"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//input[@type="checkbox"])[2]').click()
        self.driver.find_element("xpath", "//button[text()='删除']").click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info
