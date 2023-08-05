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
        self.driver.find_element("xpath", '//div[@name="category"]//input[@placeholder="请选择"]').click()
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
        time.sleep(1.1)
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

    def create_material_type_verification(self):
        """新增物料，物料类型固定选项校验"""

        self.driver.find_element("xpath", '(//div[@name="materialType"]//input)[2]').click()
        el_list = ['//ul[@role="listbox"]//li[text()="成本物料"]', '//ul[@role="listbox"]//li[text()="制造物料"]',
                   '//ul[@role="listbox"]//li[text()="采购物料"]']

        for el in el_list:

            if not self.driver.find_element("xpath", el):

                return False
        return True

    def create_material_two(self):
        """新增物料二"""

        time.sleep(1)
        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//div[@name="category"]//input[@placeholder="请选择"]').click()
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

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="specification"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="specification"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="model"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="model"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="materialQuality"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="materialQuality"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="figureNo"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="figureNo"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", '//div[text()="编辑成功"]'))
        return assert_info

    def update_material_required(self):
        """编辑物料必填"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"])[1]').click()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", '(//div[@name="materialType"]//input)[2]').click()
        self.driver.find_element("xpath", '//div[@name="materialType"]//button[@aria-label="Clear"]').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//input').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//button[@aria-label="Clear"]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="请填写该必填项"]'))
        return assert_info

    def update_name_length(self):
        """编辑名称长度校验"""

        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        return assert_info

    def update_specification_length(self):
        """编辑规格长度校验"""

        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']").clear()
        return assert_info

    def update_model_length(self):
        """编辑型号长度校验"""

        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']").clear()
        return assert_info

    def update_material_quality_length(self):
        """编辑材质长度校验"""

        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']").clear()
        return assert_info

    def update_figure_no_length(self):
        """编辑图号长度校验"""

        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']").clear()
        return assert_info

    def update_material_type_verification(self):
        """编辑物料，物料类型固定选项校验"""

        self.driver.find_element("xpath", '(//div[@name="materialType"]//input)[2]').click()
        el_list = ['//ul[@role="listbox"]//li[text()="成本物料"]', '//ul[@role="listbox"]//li[text()="制造物料"]',
                   '//ul[@role="listbox"]//li[text()="采购物料"]']

        for el in el_list:

            if not self.driver.find_element("xpath", el):

                return False
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return True

    def copy_material(self):
        """复制物料"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//span[@aria-label="复制"])[1]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", '//div[text()="新增成功"]'))
        return assert_info

    def copy_material_required(self):
        """复制物料必填"""

        self.driver.find_element("xpath", '(//span[@aria-label="复制"])[1]').click()
        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", '(//div[@name="materialType"]//input)[2]').click()
        self.driver.find_element("xpath", '//div[@name="materialType"]//button[@aria-label="Clear"]').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//input').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//button[@aria-label="Clear"]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="请填写该必填项"]'))
        return assert_info

    def copy_code_length(self):
        """复制编码长度校验"""

        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        return assert_info

    def copy_name_length(self):
        """复制名称长度校验"""

        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        return assert_info

    def copy_specification_length(self):
        """复制规格长度校验"""

        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']").clear()
        return assert_info

    def copy_model_length(self):
        """复制型号长度校验"""

        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']").clear()
        return assert_info

    def copy_material_quality_length(self):
        """复制材质长度校验"""

        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']").clear()
        return assert_info

    def copy_figure_no_length(self):
        """复制图号长度校验"""

        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']").clear()
        return assert_info

    def copy_material_type_verification(self):
        """复制物料，物料类型固定选项校验"""

        self.driver.find_element("xpath", '(//div[@name="materialType"]//input)[2]').click()
        el_list = ['//ul[@role="listbox"]//li[text()="成本物料"]', '//ul[@role="listbox"]//li[text()="制造物料"]',
                   '//ul[@role="listbox"]//li[text()="采购物料"]']

        for el in el_list:

            if not self.driver.find_element("xpath", el):

                return False
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return True

    def goto_detail_verification(self):
        """查看详情页面"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//td[@label="物料编码"]//a)[1]').click()
        assert_info = self.get_alert(("xpath", '//h6[text()="基础信息"]'))
        return assert_info

    def detail_update_material(self):
        """详情编辑物料"""

        self.driver.find_element("xpath", "//button[text()='编辑']").click()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="specification"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="specification"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="model"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="model"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="materialQuality"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="materialQuality"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="figureNo"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="figureNo"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", '//div[text()="编辑成功"]'))
        return assert_info

    def detail_update_material_required(self):
        """详情编辑物料必填"""

        time.sleep(1.5)
        self.driver.find_element("xpath", "//button[text()='编辑']").click()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", '//div[@name="materialType"]//input').click()
        self.driver.find_element("xpath", '//div[@name="materialType"]//button[@aria-label="Clear"]').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//input').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//button[@aria-label="Clear"]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="请填写该必填项"]'))
        return assert_info

    def detail_update_name_length(self):
        """详情编辑名称长度校验"""

        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        return assert_info

    def detail_update_specification_length(self):
        """详情编辑规格长度校验"""

        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']").clear()
        return assert_info

    def detail_update_model_length(self):
        """详情编辑型号长度校验"""

        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']").clear()
        return assert_info

    def detail_update_material_quality_length(self):
        """详情编辑材质长度校验"""

        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']").clear()
        return assert_info

    def detail_update_figure_no_length(self):
        """详情编辑图号长度校验"""

        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']").clear()
        return assert_info

    def detail_update_material_type_verification(self):
        """编辑物料，物料类型固定选项校验"""

        self.driver.find_element("xpath", '//div[@name="materialType"]//input').click()
        el_list = ['//ul[@role="listbox"]//li[text()="成本物料"]', '//ul[@role="listbox"]//li[text()="制造物料"]',
                   '//ul[@role="listbox"]//li[text()="采购物料"]']

        for el in el_list:

            if not self.driver.find_element("xpath", el):

                return False
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return True

    def detail_copy_material(self):
        """详情复制物料"""

        time.sleep(1)
        self.driver.find_element("xpath", "//button[text()='复制']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", '//div[text()="新增成功"]'))
        return assert_info

    def detail_copy_material_required(self):
        """详情复制物料必填"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//td[@label="物料编码"]//a)[1]').click()
        self.driver.find_element("xpath", "//button[text()='复制']").click()
        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        self.driver.find_element("xpath", '//div[@name="materialType"]//input').click()
        self.driver.find_element("xpath", '//div[@name="materialType"]//button[@aria-label="Clear"]').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//input').click()
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//button[@aria-label="Clear"]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="请填写该必填项"]'))
        return assert_info

    def detail_copy_code_length(self):
        """详情复制编码长度校验"""

        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        return assert_info

    def detail_copy_name_length(self):
        """详情复制名称长度校验"""

        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").clear()
        return assert_info

    def detail_copy_specification_length(self):
        """详情复制规格长度校验"""

        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='specification'][@placeholder='请输入']").clear()
        return assert_info

    def detail_copy_model_length(self):
        """详情复制型号长度校验"""

        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='model'][@placeholder='请输入']").clear()
        return assert_info

    def detail_copy_material_quality_length(self):
        """详情复制材质长度校验"""

        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='materialQuality'][@placeholder='请输入']").clear()
        return assert_info

    def detail_copy_figure_no_length(self):
        """详情复制图号长度校验"""

        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']")\
            .send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        self.driver.find_element("xpath", "//input[@name='figureNo'][@placeholder='请输入']").clear()
        return assert_info

    def detail_copy_material_type_verification(self):
        """详情复制物料，物料类型固定选项校验"""

        self.driver.find_element("xpath", '//div[@name="materialType"]//input').click()
        el_list = ['//ul[@role="listbox"]//li[text()="成本物料"]', '//ul[@role="listbox"]//li[text()="制造物料"]',
                   '//ul[@role="listbox"]//li[text()="采购物料"]']

        for el in el_list:

            if not self.driver.find_element("xpath", el):

                return False
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return True

    def detail_delete(self):
        """详情删除"""

        self.driver.find_element("xpath", "//button[text()='删除']").click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", '//div[text()="删除成功"]'))
        return assert_info

    def search_code(self):
        """物料编码搜索，根据输入框value值，判断查询返回的是否一致"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '//input[@name="no"]').send_keys('99999')
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="no"]')
        actual = self.get_alert(("xpath", '(//td[@label="物料编码"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def resetting_search(self):
        """重置搜索"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        el = self.driver.find_element('xpath', '//input[@name="no"]')
        assert_info = el.get_attribute('value')
        return assert_info

    def search_name(self):
        """物料名称搜索"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '//input[@name="name"]').send_keys('88888')
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="name"]')
        actual = self.get_alert(("xpath", '(//td[@label="物料描述"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def search_type(self):
        """物料类型搜索"""

        time.sleep(1)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        self.driver.find_element("xpath", '//div[@name="materialType"]//input[@role="combobox"]').click()
        self.driver.find_element("xpath", '//ul[@role="listbox"]//li[text()="成本物料"]').click()
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(("xpath", '//h6[text()="暂无数据"]'))
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        return assert_info

    def search_specification(self):
        """搜索规格"""

        time.sleep(1)
        text = self.get_alert(("xpath", '(//td[@label="规格"])[1]'))
        self.driver.find_element("xpath", '//div[@class="css-1yjo05o"]//button[@type="button"]').click()
        self.driver.find_element("xpath", '//input[@name="specification"]').send_keys(text)
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="specification"]')
        actual = self.get_alert(("xpath", '(//td[@label="规格"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:

            return False

    def search_model(self):
        """搜索型号"""

        time.sleep(1)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        text = self.get_alert(("xpath", '(//td[@label="型号"])[1]'))
        self.driver.find_element("xpath", '//input[@name="model"]').send_keys(text)
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="model"]')
        actual = self.get_alert(("xpath", '(//td[@label="型号"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def search_category(self):
        """搜索分类, 可能有多个符合的，所以不只取某个，存在即对"""
        time.sleep(1)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        self.driver.find_element("xpath", '//div[@name="category"]//input[@role="combobox"]').click()
        self.driver.find_element("xpath", '(//div[@role="button"]//input[@type="checkbox"])[1]').click()
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        time.sleep(0.5)
        expected = self.get_alert(("xpath", '//div[@name="category"]//div[@role="button"]//span'))
        actual = self.get_alert(("xpath", '//td[@label="物料分类"]'))
        if expected == actual:
            return True
        else:
            return False

    def search_quality(self):
        """搜索材质"""

        time.sleep(1)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        text = self.get_alert(("xpath", '(//td[@label="材质"])[1]'))
        self.driver.find_element("xpath", '//input[@name="materialQuality"]').send_keys(text)
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="materialQuality"]')
        actual = self.get_alert(("xpath", '(//td[@label="材质"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def search_figure_no(self):
        """搜索图号"""

        time.sleep(1)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        text = self.get_alert(("xpath", '(//td[@label="图号"])[1]'))
        self.driver.find_element("xpath", '//input[@name="figureNo"]').send_keys(text)
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="figureNo"]')
        actual = self.get_alert(("xpath", '(//td[@label="图号"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def search_signal(self):
        """搜索信号"""

        time.sleep(1)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        self.driver.find_element("xpath", '//div[@name="materialSignal"]//input').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        time.sleep(0.5)
        expected = self.get_alert(("xpath", '//div[@name="materialSignal"]//div[@role="button"]//span'))
        actual = self.get_alert(("xpath", '//td[@label="物料信号"]'))
        if expected == actual:
            return True
        else:
            return False

    def form_head_setting(self):
        """表头设置"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        self.driver.find_element("xpath", '//button[@aria-label="表头设置"]').click()
        time.sleep(1.3)
        self.driver.find_element("xpath", '//li[@data-rbd-draggable-id="materialType"]//input').click()
        self.driver.find_element("xpath", '//button[text()="确定"]').click()
        time.sleep(1)
        if self.is_el_present(("xpath", '//th[text()="物料类型"]')):
            return True
        else:
            return False

    def form_head_resetting(self):
        """表头重置"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '//button[@aria-label="表头设置"]').click()
        self.get_element(("xpath", '//button[text()="重置"]')).click()
        if self.is_el_present(("xpath", '//th[text()="物料类型"]')):
            return True
        else:
            return False

    def form_delete(self):
        """表单删除"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//span[@aria-label="删除"])[1]').click()
        self.driver.find_element("xpath", '(//button[text()="删除"])[2]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="删除成功"]'))
        return assert_info

    def batch_delete(self):
        """批量删除"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//input[@type="checkbox"])[2]').click()
        self.driver.find_element("xpath", '(//input[@type="checkbox"])[3]').click()
        self.driver.find_element("xpath", '//button[text()="删除"]').click()
        self.driver.find_element("xpath", '(//button[text()="删除"])[2]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="删除成功"]'))
        return assert_info
