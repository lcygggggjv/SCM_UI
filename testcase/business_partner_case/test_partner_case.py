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

    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增必填')
    # def test_create_partner_required(self):
    #
    #     assert_info = self.partner.create_partner_required()
    #     self.partner.assert_allure_screenshot(assert_info, "请填写该必填项")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴编码唯一性 校验')
    # def test_create_partner_code_uniqueness(self):
    #
    #     assert_info = self.partner.create_partner_code_uniqueness()
    #     self.partner.assert_allure_screenshot(assert_info, "该业务伙伴编码已存在，请重新输入")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴编码长度校验')
    # def test_create_partner_code_length(self):
    #
    #     assert_info = self.partner.create_partner_code_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴名称长度校验')
    # def test_create_partner_name_length(self):
    #
    #     assert_info = self.partner.create_partner_name_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴简称长度校验')
    # def test_create_partner_jc_length(self):
    #
    #     assert_info = self.partner.create_partner_jc_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入10个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴信用代码 长度校验')
    # def test_create_community_code_length(self):
    #
    #     assert_info = self.partner.create_community_code_length()
    #     self.partner.assert_allure_screenshot(assert_info[0], "请输入18位统一社会信用代码")
    #     self.partner.assert_allure_screenshot(assert_info[1], "请输入18位统一社会信用代码")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴营业执照 长度校验')
    # def test_create_business_license_length(self):
    #
    #     assert_info = self.partner.create_business_license_length()
    #     self.partner.assert_allure_screenshot(assert_info[0], "请输入15位或18位营业执照编号")
    #     self.partner.assert_allure_screenshot(assert_info[1], "请输入15位或18位营业执照编号")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增地址长度校验')
    # def test_create_address_length(self):
    #
    #     assert_info = self.partner.create_address_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增备注1长度校验')
    # def test_create_remark1_length(self):
    #
    #     assert_info = self.partner.create_remark1_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴联系人 长度校验')
    # def test_create_contacts_length(self):
    #
    #     assert_info = self.partner.create_contacts_length()
    #     self.partner.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴固定电话 长度校验')
    # def test_create_fixed_phone_length(self):
    #
    #     assert_info = self.partner.create_fixed_phone_length()
    #     self.partner.assert_allure_screenshot(assert_info, '请输入8个字以内的内容')
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴职位 长度校验')
    # def test_create_position_length(self):
    #
    #     assert_info = self.partner.create_position_length()
    #     self.partner.assert_allure_screenshot(assert_info, '请输入10个字以内的内容')
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增备注2, 长度校验')
    # def test_create_remark2_length(self):
    #
    #     assert_info = self.partner.create_remark2_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴手机格式 校验')
    # def test_create_phone_format(self):
    #
    #     assert_info = self.partner.create_phone_format()
    #     self.partner.assert_allure_screenshot(assert_info[0], "手机号格式错误，请重新输入")
    #     self.partner.assert_allure_screenshot(assert_info[1], "手机号格式错误，请重新输入")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='新增业务伙伴2')
    # def test_create_partner_two(self):
    #
    #     assert_info = self.partner.create_partner_two()
    #     self.partner.assert_allure_screenshot(assert_info, "新增成功")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴')
    # def test_update_partner(self):
    #
    #     assert_info = self.partner.update_partner()
    #     self.partner.assert_allure_screenshot(assert_info, "编辑成功")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴名称长度校验')
    # def test_update_partner_name_length(self):
    #
    #     assert_info = self.partner.update_partner_name_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴简称长度校验')
    # def test_update_partner_jc_length(self):
    #
    #     assert_info = self.partner.update_partner_jc_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入10个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴信用代码 长度校验')
    # def test_update_community_code_length(self):
    #
    #     assert_info = self.partner.update_community_code_length()
    #     self.partner.assert_allure_screenshot(assert_info[0], "请输入18位统一社会信用代码")
    #     self.partner.assert_allure_screenshot(assert_info[1], "请输入18位统一社会信用代码")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴营业执照 长度校验')
    # def test_update_business_license_length(self):
    #
    #     assert_info = self.partner.update_business_license_length()
    #     self.partner.assert_allure_screenshot(assert_info[0], "请输入15位或18位营业执照编号")
    #     self.partner.assert_allure_screenshot(assert_info[1], "请输入15位或18位营业执照编号")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑地址长度校验')
    # def test_update_address_length(self):
    #
    #     assert_info = self.partner.update_address_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑备注1长度校验')
    # def test_update_remark1_length(self):
    #
    #     assert_info = self.partner.update_remark1_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴联系人 长度校验')
    # def test_update_contacts_length(self):
    #
    #     assert_info = self.partner.update_contacts_length()
    #     self.partner.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴固定电话 长度校验')
    # def test_update_fixed_phone_length(self):
    #
    #     assert_info = self.partner.update_fixed_phone_length()
    #     self.partner.assert_allure_screenshot(assert_info, '请输入8个字以内的内容')
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴职位 长度校验')
    # def test_update_position_length(self):
    #
    #     assert_info = self.partner.update_position_length()
    #     self.partner.assert_allure_screenshot(assert_info, '请输入10个字以内的内容')
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑备注2, 长度校验')
    # def test_update_remark2_length(self):
    #
    #     assert_info = self.partner.update_remark2_length()
    #     self.partner.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴手机格式 校验')
    # def test_update_phone_format(self):
    #
    #     assert_info = self.partner.update_phone_format()
    #     self.partner.assert_allure_screenshot(assert_info[0], "手机号格式错误，请重新输入")
    #     self.partner.assert_allure_screenshot(assert_info[1], "手机号格式错误，请重新输入")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴编码置灰')
    # def test_update_code_disable(self):
    #
    #     assert_info = self.partner.update_code_disable()
    #     self.partner.assert_allure_screenshot(assert_info, "true")
    #
    # @pytest.mark.P2
    # @allure.testcase(url="", name='编辑业务伙伴必填')
    # def test_update_partner_required(self):
    #
    #     assert_info = self.partner.update_partner_required()
    #     self.partner.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='按钮激活业务伙伴')
    def test_open_partner(self):

        assert_info = self.partner.open_partner()
        self.partner.assert_allure_screenshot(assert_info, "活动")

    @pytest.mark.P2
    @allure.testcase(url="", name='按钮冻结业务伙伴')
    def test_close_partner(self):

        assert_info = self.partner.close_partner()
        self.partner.assert_allure_screenshot(assert_info, "冻结")

    @pytest.mark.P2
    @allure.testcase(url="", name='提示激活业务伙伴')
    def test_alert_open_partner(self):

        assert_info = self.partner.alert_open_partner()
        self.partner.assert_allure_screenshot(assert_info, "激活成功！")

    @pytest.mark.P2
    @allure.testcase(url="", name='提示冻结业务伙伴')
    def test_button_alert_partner(self):

        assert_info = self.partner.alert_close_partner()
        self.partner.assert_allure_screenshot(assert_info, "冻结成功！")

    @pytest.mark.P2
    @allure.testcase(url="", name='查看业务伙伴')
    def test_look_partner_detail(self):

        assert_info = self.partner.look_partner_detail()
        self.partner.assert_allure_screenshot(assert_info, "基础信息")

    @pytest.mark.P2
    @allure.testcase(url="", name='详情激活业务伙伴')
    def test_detail_open_partner(self):

        assert_info = self.partner.detail_open_partner()
        self.partner.assert_allure_screenshot(assert_info, "活动")

    @pytest.mark.P2
    @allure.testcase(url="", name='详情冻结业务伙伴')
    def test_detail_close_partner(self):

        assert_info = self.partner.detail_close_partner()
        self.partner.assert_allure_screenshot(assert_info, "冻结")

    @pytest.mark.P0
    @allure.testcase(url="", name='详情创建业务伙伴账号')
    def test_create_partner_account(self):

        assert_info = self.partner.create_partner_account()
        self.partner.assert_allure_screenshot(assert_info[0], "创建成功")
        self.partner.assert_allure_screenshot(assert_info[1], "复制成功")

    @pytest.mark.P1
    @allure.testcase(url="", name='重置业务伙伴账号密码')
    def test_reopen_partner_password(self):

        assert_info = self.partner.reopen_partner_password()
        self.partner.assert_allure_screenshot(assert_info, "复制")

    @pytest.mark.P1
    @allure.testcase(url="", name='详情删除业务伙伴')
    def test_detail_delete(self):

        assert_info = self.partner.detail_delete()
        self.partner.assert_allure_screenshot(assert_info, "删除成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='查询物料编码')
    def test_search_code(self):

        assert_info = self.partner.search_code()
        self.partner.assert_allure_screenshot(assert_info, "99999")

    @pytest.mark.P2
    @allure.testcase(url="", name='重置搜索')
    def test_resetting_search(self):

        assert_info = self.partner.resetting_search()
        self.partner.assert_allure_screenshot(assert_info, '')

    @pytest.mark.P0
    @allure.testcase(url="", name='查询物料简称')
    def test_search_jc_name(self):

        assert_info = self.partner.search_jc_name()
        self.partner.assert_allure_screenshot(assert_info, "scm测试")

    @pytest.mark.P0
    @allure.testcase(url="", name='查询物料全称')
    def test_search_name(self):

        assert_info = self.partner.search_name()
        self.partner.assert_allure_screenshot(assert_info, "88888")

    @pytest.mark.P0
    @allure.testcase(url="", name='删除业务伙伴')
    def test_list_delete(self):

        assert_info = self.partner.list_delete()
        self.partner.assert_allure_screenshot(assert_info, "删除成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='批量删除业务伙伴')
    def test_batch_list_delete(self):

        assert_info = self.partner.batch_list_delete()
        self.partner.assert_allure_screenshot(assert_info, "删除成功")
