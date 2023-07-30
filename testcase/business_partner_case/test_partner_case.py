import allure
import pytest
from page_manager.business_partner.partner_information_page import PartnerPage


class TestPartnerPage:

    partner = None

    @classmethod
    def setup_class(cls):

        cls.partner = PartnerPage()
        cls.partner.goto_partner_page()

    @pytest.mark.P0
    @allure.testcase(url="", name='新增业务伙伴')
    def test_create_partner(self):

        assert_info = self.partner.create_partner()
        self.partner.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增必填')
    def test_create_partner_required(self):

        assert_info = self.partner.create_partner_required()
        self.partner.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴编码唯一性 校验')
    def test_create_partner_code_uniqueness(self):

        assert_info = self.partner.create_partner_code_uniqueness()
        self.partner.assert_allure_screenshot(assert_info, "该业务伙伴编码已存在，请重新输入")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴编码长度校验')
    def test_create_partner_code_length(self):

        assert_info = self.partner.create_partner_code_length()
        self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴名称长度校验')
    def test_create_partner_name_length(self):

        assert_info = self.partner.create_partner_name_length()
        self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴简称长度校验')
    def test_create_partner_jc_length(self):

        assert_info = self.partner.create_partner_jc_length()
        self.partner.assert_allure_screenshot(assert_info, "请输入10个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴信用代码 长度校验')
    def test_create_community_code_length(self):

        assert_info = self.partner.create_community_code_length()
        self.partner.assert_allure_screenshot(assert_info[0], "请输入18位统一社会信用代码")
        self.partner.assert_allure_screenshot(assert_info[1], "请输入18位统一社会信用代码")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴营业执照 长度校验')
    def test_create_business_license_length(self):

        assert_info = self.partner.create_business_license_length()
        self.partner.assert_allure_screenshot(assert_info[0], "请输入15位或18位营业执照编号")
        self.partner.assert_allure_screenshot(assert_info[1], "请输入15位或18位营业执照编号")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增地址长度校验')
    def test_create_address_length(self):

        assert_info = self.partner.create_address_length()
        self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增备注1长度校验')
    def test_create_remark1_length(self):

        assert_info = self.partner.create_remark1_length()
        self.partner.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴联系人 长度校验')
    def test_create_contacts_length(self):

        assert_info = self.partner.create_contacts_length()
        self.partner.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴固定电话 长度校验')
    def test_create_fixed_phone_length(self):

        assert_info = self.partner.create_fixed_phone_length()
        self.partner.assert_allure_screenshot(assert_info, '请输入8个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴职位 长度校验')
    def test_create_position_length(self):

        assert_info = self.partner.create_position_length()
        self.partner.assert_allure_screenshot(assert_info, '请输入10个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url="", name='新增备注2, 长度校验')
    def test_create_remark2_length(self):

        assert_info = self.partner.create_remark2_length()
        self.partner.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴手机格式 校验')
    def test_create_phone_format(self):

        assert_info = self.partner.create_phone_format()
        self.partner.assert_allure_screenshot(assert_info[0], "手机号格式错误，请重新输入")
        self.partner.assert_allure_screenshot(assert_info[1], "手机号格式错误，请重新输入")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增业务伙伴2')
    def test_create_partner_two(self):

        assert_info = self.partner.create_partner_two()
        self.partner.assert_allure_screenshot(assert_info, "新增成功")
