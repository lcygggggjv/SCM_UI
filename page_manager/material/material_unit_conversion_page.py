import time

from common.mock import Mock
from page_manager.basepage import BasePage


class MaterialUnitConversionPage(BasePage):

    mock = Mock()

    def create_unit_conversion(self):
        """新增单位换算信息"""

        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增单位换算信息']").click()
            self.driver.find_element("xpath", '//input[@name="material.text"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@role="combobox"]').click()
            self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
            self.driver.find_element("xpath", '//input[@name="targetRatio"][@type="number"]').send_keys(10)
        elif self.is_el_present(('xpath', "//td[text()='99999'][@label='物料编码']")):

            self.driver.find_element("xpath", "//button[text()='新增单位换算信息']").click()
            self.driver.find_element("xpath", '//input[@name="material.text"]//following-sibling::div//button').click()
            time.sleep(1.5)
            self.driver.find_element("xpath", '(//input[@type="radio"])[1]').click()
            self.driver.find_element("xpath", '(//button[text()="确定"])[2]').click()
            self.driver.find_element("xpath", '//input[@role="combobox"]').click()
            self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
            self.driver.find_element("xpath", '//input[@name="targetRatio"][@type="number"]').send_keys(10)
        else:
            self.driver.find_element("xpath", "//button[text()='新增单位换算信息']").click()
            self.driver.find_element("xpath", '//input[@name="material.text"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@role="combobox"]').click()
            self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
            self.driver.find_element("xpath", '//input[@name="targetRatio"][@type="number"]').send_keys(10)
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def create_conversion_required(self):
        """新增单位换算必填"""

        self.driver.find_element("xpath", "//button[text()='新增单位换算信息']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_conversion_code_absent(self):
        """新增单位换算 物料编码不存在校验"""

        self.driver.find_element("xpath", '//input[@name="material.text"]').send_keys(self.mock.faker_pystr())
        assert_info = self.get_alert(("xpath", "//div[text()='该物料编码不存在，请重新输入']"))
        return assert_info

    def create_conversion_different(self):
        """新增单位换算，单位不与本身相同"""

        self.driver.find_element("xpath", '//input[@name="material.text"]').clear()
        self.driver.find_element("xpath", '//input[@name="material.text"]').send_keys('99999')
        self.driver.find_element('xpath', '//input[@role="combobox"]').click()
        self.driver.find_element('xpath', "//li[text()='99999']").click()
        self.driver.find_element('xpath', "//button[text()='确定']").click()
        # time.sleep(1)
        assert_info = self.get_alert(("xpath", "//div[text()='“基本单位”不得与“目标单位”相同']"))
        return assert_info

    def create_already_exists(self):
        """组合已存在"""

        self.driver.find_element('xpath', '//input[@role="combobox"]').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
        time.sleep(1)
        self.driver.find_element('xpath', "//button[text()='确定']").click()
        time.sleep(1)
        assert_info = self.get_alert(("xpath", "//div[text()='“物料编码+基本单位”组合已存在，请重新选择']"))
        return assert_info

    def create_conversion_coefficient(self):
        """新增单位换算系数，小数3位校验"""

        time.sleep(1)
        self.driver.find_element("xpath", '//input[@name="targetRatio"][@type="number"]').send_keys(3.1234)
        assert_info = self.get_alert(("xpath", '//div[text()="小数最多保留小数点后3位"]'))
        return assert_info

    def create_conversion_disable_verification(self):
        """新增单位换算， disabled属性校验
        循环遍历el_list中的XPath，对于每个XPath，获取相应的元素并判断disabled属性。
        如果任何一个元素的disabled属性不为真，则立即返回False，表示存在未被禁用的元素。
        只有当所有元素的disabled属性都为真时，才会执行到循环外部的return True语句，表示所有元素都处于禁用状态。
        """
        time.sleep(1)
        el_list = ['//input[@name="name"]', '//input[@name="specification"]', '//input[@name="model"]',
                   '//input[@name="baseRatio"]', '//input[@name="targetRatio"][@type="text"]']

        for xpath in el_list:
            el = self.driver.find_element('xpath', xpath)
            if not el.get_attribute('disabled'):
                return False
        return True

    def create_detail_search_code(self):
        """详情搜索物料编码"""

        time.sleep(2)
        self.driver.find_element("xpath", '(//input[@name="material.text"]//following-sibling::div//button)[2]').click()

        self.driver.find_element("xpath", '//input[@name="no"]').send_keys('99999')
        self.driver.find_element('xpath', '(//button[@aria-label="查询"])[2]').click()
        el = self.driver.find_element("xpath", '//input[@name="no"]')
        actual = self.get_alert(("xpath", '(//td[@label="物料编码"][text()="99999"])[2]'))
        if el.get_attribute("value") == actual:
            return True
        else:

            return False

    def create_detail_search_name(self):
        """详情搜索物料名称"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//button[@aria-label="重置"])[2]').click()
        time.sleep(1)
        self.driver.find_element("xpath", '(//input[@name="name"])[2]').send_keys('88888')
        self.driver.find_element('xpath', '(//button[@aria-label="查询"])[2]').click()
        el = self.driver.find_element("xpath", '//input[@name="name"]')
        actual = self.get_alert(("xpath", '(//td[@label="物料描述"][text()="88888"])[2]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def create_conversion_two(self):
        """新增单位系数2"""

        self.driver.find_element("xpath", "(//button[text()='取消'])[2]").click()
        self.driver.find_element("xpath", '//button[text()="取消"]').click()
        # time.sleep(1)
        self.driver.find_element("xpath", "//button[text()='新增单位换算信息']").click()
        self.driver.find_element("xpath", '//input[@name="material.text"]//following-sibling::div//button').click()
        time.sleep(1.5)
        self.driver.find_element("xpath", '(//input[@type="radio"])[1]').click()
        self.driver.find_element("xpath", '(//button[text()="确定"])[2]').click()
        self.driver.find_element("xpath", '//input[@role="combobox"]').click()
        self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
        self.driver.find_element("xpath", '//input[@name="targetRatio"][@type="number"]').send_keys(10)
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))
        return assert_info

    def search_conversion_unit(self):
        """精确搜索基本单位"""

        time.sleep(1)
        text = self.get_alert(("xpath", '(//td[@label="基本单位"])[1]'))
        self.driver.find_element('xpath', '//input[@name="baseUnit"]').send_keys(text)
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="baseUnit"]')
        actual = self.get_alert(("xpath", '(//td[@label="基本单位"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def conversion_resetting_search(self):
        """重置搜索"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        el = self.driver.find_element('xpath', '//input[@name="baseUnit"]')
        assert_info = el.get_attribute('value')
        return assert_info

    def search_conversion_target_unit(self):
        """精确搜索目标单位"""

        time.sleep(1.5)
        text = self.get_alert(("xpath", '(//td[@label="目标单位"])[1]'))
        self.driver.find_element('xpath', '//input[@name="targetUnit"]').send_keys(text)
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        el = self.driver.find_element("xpath", '//input[@name="targetUnit"]')
        actual = self.get_alert(("xpath", '(//td[@label="目标单位"])[1]'))
        if el.get_attribute("value") == actual:
            return True
        else:
            return False

    def search_conversion_material_code(self):
        """精确搜索物料编码"""

        time.sleep(1.5)
        self.driver.find_element('xpath', '//input[@name="materialNo"]').send_keys('99999')
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='99999'][@label='物料编码']"))
        return assert_info

    def search_conversion_material_name(self):
        """精确搜索物料名称"""

        time.sleep(1.5)
        self.driver.find_element('xpath', '//button[@aria-label="查询"]'
                                          '//following-sibling::button[@type="button"]').click()
        self.driver.find_element('xpath', '//input[@name="materialName"]').send_keys('88888')
        self.driver.find_element('xpath', '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(('xpath', "//td[text()='88888'][@label='物料描述']"))
        return assert_info

    def delete_conversion(self):
        """删除物料单位换算"""

        # time.sleep(1.5)
        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        self.driver.find_element("xpath", '(//span[@aria-label="删除"])[1]').click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info

    def batch_delete_conversion(self):
        """批量删除单位换算"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="勾选当页"])[1]').click()
        self.driver.find_element("xpath", "//button[text()='删除']").click()
        self.driver.find_element("xpath", "(//button[text()='删除'])[2]").click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))
        return assert_info
