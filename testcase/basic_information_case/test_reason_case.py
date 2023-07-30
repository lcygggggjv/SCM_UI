import allure
import pytest
from page_manager.basic_information.reason_page import ReasonPage


class TestReason:

    reason = None

    @classmethod
    def setup_class(cls):

        cls.reason = ReasonPage()
        cls.reason.goto_reason_page()

    @pytest.mark.P0
    @allure.testcase(url="", name='新增原因')
    def test_create_reason(self):

        assert_info = self.reason.create_reason()
        self.reason.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增原因必填')
    def test_create_reason_required(self):

        assert_info = self.reason.create_reason_required()
        self.reason.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增原因编码长度校验')
    def test_create_currency_code_length(self):

        assert_info = self.reason.create_reason_code_length()
        self.reason.assert_allure_screenshot(assert_info, "请输入5个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增原因名称长度校验')
    def test_create_reason_name_length(self):

        assert_info = self.reason.create_reason_name_length()
        self.reason.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增原因编码唯一性校验')
    def test_create_reason_code_uniqueness(self):

        assert_info = self.reason.create_reason_code_uniqueness()
        self.reason.assert_allure_screenshot(assert_info, "该原因编码已存在，请重新输入")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增原因2')
    def test_create_reason_two(self):

        assert_info = self.reason.create_reason_two()
        self.reason.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='编辑原因')
    def test_update_reason(self):

        assert_info = self.reason.update_reason()
        self.reason.assert_allure_screenshot(assert_info, "编辑成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑原因名称必填')
    def test_update_reason_required(self):

        assert_info = self.reason.update_reason_required()
        self.reason.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑原因编码，类型disabled校验')
    def test_update_reason_code_type_disable(self):

        assert_info = self.reason.update_reason_code_type_disable()
        self.reason.assert_allure_screenshot(assert_info, True)

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑原因名称长度校验')
    def test_update_reason_name_length(self):

        assert_info = self.reason.update_reason_name_length()
        self.reason.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索原因编码')
    def test_search_reason_code(self):

        assert_info = self.reason.search_reason_code()
        self.reason.assert_allure_screenshot(assert_info, '99999')

    @pytest.mark.P2
    @allure.testcase(url="", name='重置搜索')
    def test_resetting_search(self):

        assert_info = self.reason.resetting_search()
        self.reason.assert_allure_screenshot(assert_info, '')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索原因名称')
    def test_search_reason_name(self):

        assert_info = self.reason.search_reason_name()
        self.reason.assert_allure_screenshot(assert_info, '88888')

    @pytest.mark.P2
    @allure.testcase(url="", name='搜索原因类型')
    def test_search_reason_type(self):

        assert_info = self.reason.search_reason_type()
        self.reason.assert_allure_screenshot(assert_info, '取消')

    @pytest.mark.P0
    @allure.testcase(url="", name='删除原因')
    def test_delete_reason(self):

        assert_info = self.reason.delete_reason()
        self.reason.assert_allure_screenshot(assert_info, '删除成功')

    @pytest.mark.P2
    @allure.testcase(url="", name='批量删除原因')
    def test_batch_delete_reason(self):

        assert_info = self.reason.batch_delete_reason()
        self.reason.assert_allure_screenshot(assert_info, '删除成功')
