import time

from page_manager.basepage import BasePage
from common.mock import Mock


class MaterialPage(BasePage):

    mock = Mock()

    def create_material(self):
        """新增物料"""
        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增物料']").click()
            self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").send_keys('99999')
            self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").send_keys('88888')

        elif self.is_el_present(('xpath', '//td[@label="物料编码"]//a[text()="99999"]')):
            self.driver.find_element("xpath", "//button[text()='新增物料']").click()
            self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']")\
                .send_keys(self.mock.faker_pystr())
            self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
                .send_keys(self.mock.faker_pystr())
        else:
            self.driver.find_element("xpath", "//button[text()='新增物料']").click()
            self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").send_keys('99999')
            self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").send_keys('88888')
        self.driver.find_element("xpath", '//input[@aria-autocomplete="list"][@placeholder="请选择"]').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]//div[@role="button"]').click()
        self.driver.find_element("xpath", '//div[@name="materialSignal"]//input[@placeholder="请选择"]').click()
        self.driver.find_element("xpath", '//ul[@role="listbox"]//li[@tabindex="-1"]').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//input').click()
        self.driver.find_element("xpath", '//li[@role="option"][@tabindex="-1"]').click()

        self.driver.find_element("xpath", '//input[@name="specification"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="model"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="materialQuality"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="figureNo"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", '//div[text()="新增成功"]'))
        return assert_info

    def create_material_required(self):
        """新增必填"""

        self.driver.find_element("xpath", "//button[text()='新增物料']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_material_uniqueness(self):
        """新增唯一"""

        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").send_keys('99999')
        time.sleep(1.3)
        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").send_keys('99999')
        assert_info = self.get_alert(("xpath", "//div[text()='该物料编码已存在，请重新输入']"))
        return assert_info

    def create_code_length(self):
        """新增编码长度校验"""

        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").clear()
        return assert_info

    def create_name_length(self):
        """新增名称长度校验"""

        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        return assert_info

    def create_specification_length(self):
        """新增规格长度校验"""

        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']").clear()
        return assert_info

    def create_model_length(self):
        """新增型号长度校验"""

        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']").clear()
        return assert_info

    def create_material_quality_length(self):
        """新增材质长度校验"""

        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']").clear()
        return assert_info

    def create_figure_no_length(self):
        """新增图号长度校验"""

        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']").clear()
        return assert_info

    def create_material_two(self):
        """新增物料二"""

        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@aria-autocomplete="list"][@placeholder="请选择"]').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]//div[@role="button"]').click()
        self.driver.find_element("xpath", '//div[@name="materialSignal"]//input[@placeholder="请选择"]').click()
        self.driver.find_element("xpath", '//ul[@role="listbox"]//li[@tabindex="-1"]').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//input').click()
        self.driver.find_element("xpath", '//li[@role="option"][@tabindex="-1"]').click()
        self.driver.find_element("xpath", '//input[@name="specification"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="model"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="materialQuality"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="figureNo"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", '//div[text()="新增成功"]'))
        return assert_info

    def update_material(self):
        """编辑物料"""

        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        pass
