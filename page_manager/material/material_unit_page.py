import time

from common.mock import Mock
from page_manager.basepage import BasePage


class MaterialUnitPage(BasePage):

    def create_unit(self):
        """新增物料单位"""

        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增单位信息']").click()
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('99999')

        elif self.is_el_present(('xpath', "//td[text()='99999'][@label='单位名称']")):
            self.driver.find_element("xpath", "//button[text()='新增单位信息']").click()
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())

        else:

            self.driver.find_element("xpath", "//button[text()='新增单位信息']").click()
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('99999')

        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys(
            Mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="remark"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_unit_required(self):
        """新增单位必填"""

        self.driver.find_element("xpath", "//button[text()='新增单位信息']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_unit_name_length(self):
        """新增单位名称长度校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.mock_data())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入5个字以内的内容']"))
        return assert_info

    def create_unit_jc_length(self):
        """新增单位简称长度校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys(
            Mock.mock_data())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入5个字以内的内容']"))
        return assert_info

    def create_unit_remark_length(self):
        """新增单位备注长度校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="remark"]').send_keys(Mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        return assert_info

    def create_unit_uniqueness(self):
        """新增单位名称唯一性"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('99999')
        assert_info = self.get_alert(("xpath", "//div[text()='该单位名称已存在，请重新输入']"))
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def create_unit_two(self):
        """新增单位2"""

        self.driver.find_element("xpath", "//button[text()='新增单位信息']").click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys(
            Mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_unit_three(self):
        """新增单位3"""

        self.driver.find_element("xpath", "//button[text()='新增单位信息']").click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys(
            Mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def update_unit(self):
        """编辑单位"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="remark"]').clear()
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys(
            Mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="remark"]').send_keys(Mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='编辑成功']"))
        return assert_info

    def update_unit_jc_length(self):
        """编辑单位简称，长度校验"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys(Mock.mock_data())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入5个字以内的内容']"))
        return assert_info

    def update_unit_remark_length(self):
        """编辑单位备注，长度校验"""

        self.get_element(("xpath", '//input[@name="remark"]')).clear()
        self.get_element(("xpath", '//input[@name="remark"]')).send_keys(Mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        return assert_info

    def update_unit_disable(self):
        """编辑单位名称置灰属性"""

        el = self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')
        assert_info = el.get_attribute("disabled")
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def delete_unit(self):
        """删除单位"""

        self.driver.find_element("xpath", '(//span[@aria-label="删除"])[1]').click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info

    def batch_delete_unit(self):
        """批量删除单位"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//input[@type="checkbox"])[2]').click()
        self.driver.find_element("xpath", "//button[text()='删除']").click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info
