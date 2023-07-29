import allure
import pytest
from page_manager.basic_information.currency_page import CurrencyPage


class TestCurrency:

    currency = None

    @classmethod
    def setup_class(cls):

        cls.currency = CurrencyPage()
        cls.currency.goto_currency_page()

    @pytest.mark.P0
    @allure.testcase(url="", name='新增币种')
    def test_create_currency(self):

        assert_info = self.currency.create_currency()
        self.currency.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增币种必填')
    def test_create_currency_required(self):

        assert_info = self.currency.create_currency_required()
        self.currency.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增币种编码长度校验')
    def test_create_currency_code_length(self):

        assert_info = self.currency.create_currency_code_length()
        self.currency.assert_allure_screenshot(assert_info, "请输入5个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增币种名称长度校验')
    def test_create_currency_name_length(self):

        assert_info = self.currency.create_currency_name_length()
        self.currency.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增币种编码唯一性校验')
    def test_create_currency_code_uniqueness(self):

        assert_info = self.currency.create_currency_code_uniqueness()
        self.currency.assert_allure_screenshot(assert_info, "该币种编码已存在，请重新输入")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增币种2')
    def test_create_currency_two(self):

        assert_info = self.currency.create_currency_two()
        self.currency.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='设置默认币种')
    def test_setting_default_currency(self):

        assert_info = self.currency.setting_default_currency()
        self.currency.assert_allure_screenshot(assert_info, "设置默认币种成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='编辑币种')
    def test_update_currency(self):

        assert_info = self.currency.update_currency()
        self.currency.assert_allure_screenshot(assert_info, "编辑成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑币种名称必填')
    def test_update_currency_required(self):

        assert_info = self.currency.update_currency_required()
        self.currency.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑币种名称长度校验')
    def test_update_currency_length(self):

        assert_info = self.currency.update_currency_length()
        self.currency.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑币种编码disabled校验')
    def test_update_currency_code_disable(self):

        assert_info = self.currency.update_currency_code_disable()
        self.currency.assert_allure_screenshot(assert_info, 'true')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索币种编码')
    def test_search_currency_code(self):

        assert_info = self.currency.search_currency_code()
        self.currency.assert_allure_screenshot(assert_info, '99999')

    @pytest.mark.P2
    @allure.testcase(url="", name='重置搜索币种编码')
    def test_currency_resetting_search(self):

        assert_info = self.currency.currency_resetting_search()
        self.currency.assert_allure_screenshot(assert_info, '')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索币种名称')
    def test_search_currency_name(self):

        assert_info = self.currency.search_currency_name()
        self.currency.assert_allure_screenshot(assert_info, '88888')

    @pytest.mark.P0
    @allure.testcase(url="", name='删除币种')
    def test_delete_currency(self):

        assert_info = self.currency.delete_currency()
        self.currency.assert_allure_screenshot(assert_info, '删除成功')

    @pytest.mark.P2
    @allure.testcase(url="", name='批量删除币种')
    def test_batch_delete_currency(self):

        assert_info = self.currency.batch_delete_currency()
        self.currency.assert_allure_screenshot(assert_info, '删除成功')
