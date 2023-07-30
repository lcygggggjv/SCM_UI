
import time
from common.mock import Mock
from page_manager.basepage import BasePage


class PartnerPage(BasePage):

    mock = Mock()

    def create_tax_rate(self):
        """新增税率"""

        time.sleep(0.5)
        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增业务伙伴信息']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
        elif self.is_el_present(('xpath', '//td[@label="业务伙伴编码"]//a[text()="99999"]')):
            self.driver.find_element("xpath", "//button[text()='新增业务伙伴信息']").click()
            self.driver.find_element("xpath", '//input[@name="rate"]').send_keys(self.mock.faker_pystr())
        else:
            self.driver.find_element("xpath", "//button[text()='新增业务伙伴信息']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
        self.driver.find_element("xpath", '(//div[@name="partnerType"]//input[@type="checkbox"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="expectedAt"]').click()
        self.driver.find_element("xpath", '(//button[@role="gridcell"][text()="1"])[1]').click()
        self.driver.find_element("xpath", '(//button[@role="gridcell"][text()="28"])[2]').click()
        self.driver.find_element("xpath", '//div[@name="defaultCurrency"]//input[@role="combobox"]').click()

        self.driver.find_element("xpath", '//li[@data-option-index="0"]').click()
        self.driver.find_element("xpath", '//input[@name="creditCode"]').send_keys(self.mock.faker_num_18())
        self.driver.find_element("xpath", '//input[@name="licenseCode"]').send_keys(self.mock.faker_num_18())
        self.driver.find_element("xpath", '//div[@name="companyAddr"]//input[@role="combobox"]').click()
        self.driver.find_element("xpath", '//span[text()="中国香港"]').click()

        self.driver.find_element("xpath", '//input[@name="address"]').send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="remark"]').send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="contactList.0.name"]').send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').send_keys(self.mock.rand_phone_num())
        self.driver.find_element("xpath", '//input[@name="contactList.0.fixedPhone"]').send_keys(self.mock.ran_phone2())
        self.driver.find_element("xpath", '//input[@name="contactList.0.position"]').send_keys(self.mock.faker_pystr())
        self.driver.find_element("xpath", '//input[@name="contactList.0.remark"]').send_keys(self.mock.faker_pystr())
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
