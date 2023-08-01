
import time
from common.mock import Mock
from page_manager.basepage import BasePage


class PartnerPage(BasePage):

    """业务伙伴编码唯一性，需要需要停留1秒，清除，再输入才提示"""

    mock = Mock()

    def create_partner(self):
        """新增业务伙伴"""

        time.sleep(0.5)
        if self.is_el_present(("xpath", "//h6[text()='暂无数据']")):
            self.driver.find_element("xpath", "//button[text()='新增业务伙伴信息']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('88888')
            self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys('scm测试')

        elif self.is_el_present(('xpath', '//td[@label="业务伙伴编码"]//a[text()="99999"]')):
            self.driver.find_element("xpath", "//button[text()='新增业务伙伴信息']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]')\
                .send_keys(self.mock.faker_pystr())
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]') \
                .send_keys(self.mock.faker_pystr())
            self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]') \
                .send_keys(self.mock.faker_pystr())

        else:
            self.driver.find_element("xpath", "//button[text()='新增业务伙伴信息']").click()
            self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
            self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').send_keys('88888')
            self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').send_keys('scm测试')

        self.driver.find_element("xpath", '(//div[@name="partnerType"]//input[@type="checkbox"])[1]').click()
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

    def create_partner_required(self):
        """新增业务伙伴必填"""

        self.driver.find_element("xpath", "//button[text()='新增业务伙伴信息']").click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        return assert_info

    def create_partner_code_uniqueness(self):
        """新增业务伙伴编码唯一性 校验"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
        time.sleep(1)
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys('99999')
        assert_info = self.get_alert(("xpath", "//div[text()='该业务伙伴编码已存在，请重新输入']"))
        return assert_info

    def create_partner_code_length(self):
        """新增业务伙伴编码长度 校验"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def create_partner_name_length(self):
        """新增业务伙伴名称 长度 校验"""

        # self.double_click_delete('//input[@name="rate"]')
        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def create_partner_jc_length(self):
        """新增业务伙伴简称 长度 校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入10个字以内的内容']"))
        return assert_info

    def create_community_code_length(self):
        """新增业务伙伴信用代码 长度校验"""

        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="creditCode"]').send_keys(1)
        assert_info1 = self.get_alert(("xpath", "//div[text()='请输入18位统一社会信用代码']"))
        self.driver.find_element("xpath", '//input[@name="creditCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="creditCode"]').send_keys(self.mock.faker_pystr_21())
        assert_info2 = self.get_alert(("xpath", "//div[text()='请输入18位统一社会信用代码']"))
        return assert_info1, assert_info2

    def create_business_license_length(self):
        """新增业务伙伴营业执照 长度校验"""

        self.driver.find_element("xpath", '//input[@name="creditCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="licenseCode"]').send_keys(1)
        assert_info1 = self.get_alert(("xpath", "//div[text()='请输入15位或18位营业执照编号']"))
        self.driver.find_element("xpath", '//input[@name="licenseCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="licenseCode"]').send_keys(self.mock.faker_pystr_21())
        assert_info2 = self.get_alert(("xpath", "//div[text()='请输入15位或18位营业执照编号']"))
        return assert_info1, assert_info2

    def create_address_length(self):
        """新增业务伙伴地址 长度校验"""

        self.driver.find_element("xpath", '//input[@name="licenseCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="address"]').send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def create_remark1_length(self):
        """新增业务伙伴备注1 长度校验"""

        self.driver.find_element("xpath", '//input[@name="address"]').clear()
        self.driver.find_element("xpath", '//input[@name="remark"]').send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        return assert_info

    def create_contacts_length(self):
        """新增业务伙伴联系人 长度校验"""

        self.driver.find_element("xpath", '//input[@name="remark"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.name"]').send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def create_fixed_phone_length(self):
        """新增业务伙伴固定电话 长度校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.name"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.fixedPhone"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入8个字以内的内容']"))
        return assert_info

    def create_position_length(self):
        """新增业务伙伴职位 长度校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.fixedPhone"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.position"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入10个字以内的内容']"))
        return assert_info

    def create_remark2_length(self):
        """新增业务伙伴备注1 长度校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.position"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.remark"]').send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        return assert_info

    def create_phone_format(self):
        """新增业务伙伴手机格式 校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.remark"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').send_keys(1)
        assert_info1 = self.get_alert(("xpath", "//div[text()='手机号格式错误，请重新输入']"))
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').send_keys(self.mock.faker_pystr_21())
        assert_info2 = self.get_alert(("xpath", "//div[text()='手机号格式错误，请重新输入']"))
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').clear()
        return assert_info1, assert_info2

    def create_partner_two(self):
        """新增业务伙伴2"""

        self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]').send_keys(self.mock.faker_pystr())
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

    def update_partner(self):
        """编辑业务伙伴"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"]//button)[1]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='编辑成功']"))
        return assert_info

    def update_partner_name_length(self):
        """编辑业务伙伴名称 长度 校验"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"]//button)[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def update_partner_jc_length(self):
        """编辑业务伙伴简称 长度 校验"""

        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入10个字以内的内容']"))
        return assert_info

    def update_community_code_length(self):
        """编辑业务伙伴信用代码 长度校验"""

        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="creditCode"]').send_keys(1)
        assert_info1 = self.get_alert(("xpath", "//div[text()='请输入18位统一社会信用代码']"))
        self.driver.find_element("xpath", '//input[@name="creditCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="creditCode"]').send_keys(self.mock.faker_pystr_21())
        assert_info2 = self.get_alert(("xpath", "//div[text()='请输入18位统一社会信用代码']"))
        return assert_info1, assert_info2

    def update_business_license_length(self):
        """编辑业务伙伴营业执照 长度校验"""

        self.driver.find_element("xpath", '//input[@name="creditCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="licenseCode"]').send_keys(1)
        assert_info1 = self.get_alert(("xpath", "//div[text()='请输入15位或18位营业执照编号']"))
        self.driver.find_element("xpath", '//input[@name="licenseCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="licenseCode"]').send_keys(self.mock.faker_pystr_21())
        assert_info2 = self.get_alert(("xpath", "//div[text()='请输入15位或18位营业执照编号']"))
        return assert_info1, assert_info2

    def update_address_length(self):
        """编辑业务伙伴地址 长度校验"""

        self.driver.find_element("xpath", '//input[@name="licenseCode"]').clear()
        self.driver.find_element("xpath", '//input[@name="address"]').send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def update_remark1_length(self):
        """编辑业务伙伴备注1 长度校验"""

        self.driver.find_element("xpath", '//input[@name="address"]').clear()
        self.driver.find_element("xpath", '//input[@name="remark"]').send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        return assert_info

    def update_contacts_length(self):
        """编辑业务伙伴联系人 长度校验"""

        self.driver.find_element("xpath", '//input[@name="remark"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.name"]').send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))
        return assert_info

    def update_fixed_phone_length(self):
        """编辑业务伙伴固定电话 长度校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.name"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.fixedPhone"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入8个字以内的内容']"))
        return assert_info

    def update_position_length(self):
        """编辑业务伙伴职位 长度校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.fixedPhone"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.position"]')\
            .send_keys(self.mock.faker_pystr_21())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入10个字以内的内容']"))
        return assert_info

    def update_remark2_length(self):
        """编辑业务伙伴备注2 长度校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.position"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.remark"]').send_keys(self.mock.faker_data_61())
        assert_info = self.get_alert(("xpath", "//div[text()='请输入60个字以内的内容']"))
        return assert_info

    def update_phone_format(self):
        """编辑业务伙伴手机格式 校验"""

        self.driver.find_element("xpath", '//input[@name="contactList.0.remark"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').send_keys(1)
        assert_info1 = self.get_alert(("xpath", "//div[text()='手机号格式错误，请重新输入']"))
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').send_keys(self.mock.faker_pystr_21())
        assert_info2 = self.get_alert(("xpath", "//div[text()='手机号格式错误，请重新输入']"))
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').clear()
        return assert_info1, assert_info2

    def update_code_disable(self):
        """业务伙伴编码置灰"""

        el = self.driver.find_element("xpath", '//input[@name="no"][@placeholder="请输入"]')
        assert_info = el.get_attribute('disabled')
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def update_partner_required(self):
        """编辑必填"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//span[@aria-label="编辑"]//button//*[name()="svg"])[1]').click()
        self.driver.find_element("xpath", '//input[@name="name"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="abbreviation"][@placeholder="请输入"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.name"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.phone"]').clear()
        self.driver.find_element("xpath", '//input[@name="contactList.0.position"]').clear()
        self.move_to_el(("xpath", '(//input[@name="expectedAt"]//following-sibling::div//button)[1]'))
        self.driver.find_element("xpath", '(//input[@name="expectedAt"]//following-sibling::div//button)[1]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))
        self.driver.find_element("xpath", "//button[text()='取消']").click()
        return assert_info

    def open_partner(self):
        """按钮激活业务伙伴"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//span[@class="MuiSwitch-root MuiSwitch-'
                                          'sizeMedium css-g1zaqd"])[1]').click()
        time.sleep(1)
        assert_info = self.get_alert(("xpath", '(//td[@label="状态"]//span)[1]'))
        return assert_info

    def close_partner(self):
        """按钮关闭业务伙伴"""

        self.driver.find_element("xpath", '(//span[@class="MuiSwitch-root MuiSwitch-'
                                          'sizeMedium css-g1zaqd"])[1]').click()
        time.sleep(1)
        assert_info = self.get_alert(("xpath", '(//td[@label="状态"]//span)[1]'))
        return assert_info

    def alert_open_partner(self):
        """提示激活业务伙伴"""

        self.driver.find_element("xpath", '(//input[@class="PrivateSwitchBase-input css-1m9pwf3"])[2]').click()
        self.driver.find_element("xpath", '//button[text()="激活"]').click()
        self.driver.find_element("xpath", '(//button[text()="激活"])[2]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="激活成功！"]'))
        return assert_info

    def alert_close_partner(self):
        """提示冻结业务伙伴"""

        self.driver.find_element("xpath", '(//input[@class="PrivateSwitchBase-input css-1m9pwf3"])[2]').click()
        self.driver.find_element("xpath", '//button[text()="冻结"]').click()
        self.driver.find_element("xpath", '(//button[text()="冻结"])[2]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="冻结成功！"]'))
        return assert_info

    def look_partner_detail(self):
        """查看业务伙伴详情"""

        time.sleep(1.5)
        self.driver.find_element("xpath", '(//td[@label="业务伙伴编码"]//a)[1]').click()
        assert_info = self.get_alert(("xpath", '//h6[text()="基础信息"]'))
        return assert_info

    def detail_open_partner(self):
        """详情激活业务伙伴"""

        self.driver.find_element("xpath", '//button[text()="全局配置信息"]').click()
        self.driver.find_element("xpath", '(//span[@class="MuiSwitch-root MuiSwitch-'
                                          'sizeMedium css-g1zaqd"])[1]').click()
        assert_info = self.get_alert(("xpath", '//span[text()="活动"]'))
        return assert_info

    def detail_close_partner(self):
        """详情冻结业务伙伴"""

        self.driver.find_element("xpath", '(//span[@class="MuiSwitch-root MuiSwitch-'
                                          'sizeMedium css-g1zaqd"])[1]').click()
        assert_info = self.get_alert(("xpath", '//span[text()="冻结"]'))
        return assert_info

    def create_partner_account(self):
        """创建业务伙伴主账号"""

        self.driver.find_element("xpath", '//button[text()="创建账号"]').click()
        self.driver.find_element("xpath", '//input[@name="account"]').clear()
        self.driver.find_element("xpath", '//input[@name="account"]').send_keys(self.mock.mock_data())
        self.driver.find_element("xpath", '//input[@name="password"]').send_keys('teletraan')
        self.driver.find_element("xpath", '//input[@name="email"]').send_keys(self.mock.ran_email())
        self.driver.find_element("xpath", '//button[text()="确定"]').click()
        time.sleep(1)
        assert_info1 = self.get_alert(("xpath", '//div[text()="创建成功"]'))
        self.driver.find_element("xpath", '//button[text()="复制"]').click()
        assert_info2 = self.get_alert(("xpath", '//div[text()="复制成功"]'))
        return assert_info1, assert_info2

    def reopen_partner_password(self):
        """重置密码"""

        self.driver.find_element("xpath", '//button[text()="全局配置信息"]').click()
        self.driver.find_element("xpath", '//button[text()="重置密码"]').click()
        self.driver.find_element("xpath", '//button[text()="重置"]').click()
        assert_info = self.get_alert(("xpath", '//button[text()="复制"]'))
        self.driver.find_element("xpath", '//button[text()="复制"]').click()
        return assert_info

    def detail_delete(self):
        """详情删除"""

        self.driver.find_element("xpath", '//button[text()="删除"]').click()
        self.driver.find_element("xpath", '(//button[text()="删除"])[2]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="删除成功"]'))
        return assert_info

    def search_code(self):
        """物料编码搜索"""

        self.driver.find_element("xpath", '//input[@name="no"]').send_keys('99999')
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(("xpath", '//td[@label="业务伙伴编码"]//a[text()="99999"]'))
        return assert_info

    def resetting_search(self):
        """重置搜索"""

        self.driver.find_element("xpath", '//button[@aria-label="重置"]').click()
        el = self.driver.find_element('xpath', '//input[@name="search"]')
        assert_info = el.get_attribute('value')
        return assert_info

    def search_jc_name(self):
        """物料物料简称搜索"""

        self.driver.find_element("xpath", '//input[@name="abbreviation"]').send_keys('scm测试')
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(("xpath", '//td[@label="业务伙伴简称"]//a[text()="scm测试"]'))
        return assert_info

    def search_name(self):
        """物料物料全称搜索"""

        self.driver.find_element("xpath", '//input[@name="name"]').send_keys('88888')
        self.driver.find_element("xpath", '//button[@aria-label="查询"]').click()
        assert_info = self.get_alert(("xpath", '//td[@label="业务伙伴全称"]//a[text()="88888"]'))
        return assert_info

    def list_delete(self):
        """表单删除"""

        self.driver.find_element("xpath", '(//span[@aria-label="删除"]//button)[1]').click()
        self.driver.find_element("xpath", '(//button[text()="删除"])[2]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="删除成功"]'))
        return assert_info

    def batch_list_delete(self):
        """批量删除"""

        time.sleep(1)
        self.driver.find_element("xpath", '(//input[@class="PrivateSwitchBase-input css-1m9pwf3"])[2]').click()
        self.driver.find_element("xpath", '//button[text()="删除"]').click()
        self.driver.find_element("xpath", '(//button[text()="删除"])[2]').click()
        assert_info = self.get_alert(("xpath", '//div[text()="删除成功"]'))
        return assert_info
