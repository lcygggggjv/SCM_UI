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

