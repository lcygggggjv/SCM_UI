import allure
import pytest
from page_manager.basic_information.tax_rate_page import TaxRatePage


class TestTaxRate:

    tax = None

    @classmethod
    def setup_class(cls):

        cls.tax = TaxRatePage()
        cls.tax.goto_tax_rate_page()

    @pytest.mark.P0
    @allure.testcase(url="", name='新增税率')
    def test_create_tax_rate(self):

        assert_info = self.tax.create_tax_rate()
        self.tax.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增税率必填')
    def test_create_tax_rate_required(self):

        assert_info = self.tax.create_tax_rate_required()
        self.tax.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增税率负数校验')
    def test_create_tax_negative_num(self):

        assert_info = self.tax.create_tax_negative_num()
        self.tax.assert_allure_screenshot(assert_info, "请输入0~99的整数")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增税率100校验')
    def test_create_tax_most_num(self):

        assert_info = self.tax.create_tax_most_num()
        self.tax.assert_allure_screenshot(assert_info, "请输入0~99的整数")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增税率 输入字符串等校验')
    def test_create_tax_str(self):

        assert_info = self.tax.create_tax_str()
        self.tax.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增税率 小数等校验')
    def test_create_tax_float(self):

        assert_info = self.tax.create_tax_float()
        self.tax.assert_allure_screenshot(assert_info, "请输入0~99的整数")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增税率唯一性校验')
    def test_create_tax_uniqueness(self):

        assert_info = self.tax.create_tax_uniqueness()
        self.tax.assert_allure_screenshot(assert_info, "该税率已存在，请重新输入")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增税率2')
    def test_create_tax_rate_two(self):

        assert_info = self.tax.create_tax_rate_two()
        self.tax.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='打开生效开关')
    def test_open_checkbox(self):

        assert_info = self.tax.open_checkbox()
        self.tax.assert_allure_screenshot(assert_info, "生效成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索税率')
    def test_search_tax_rate(self):

        assert_info = self.tax.search_tax_rate()
        self.tax.assert_allure_screenshot(assert_info, '9')

    @pytest.mark.P2
    @allure.testcase(url="", name='重置搜索')
    def test_resetting_search(self):

        assert_info = self.tax.resetting_search()
        self.tax.assert_allure_screenshot(assert_info, '')

    @pytest.mark.P0
    @allure.testcase(url="", name='删除税率')
    def test_delete_tax_rate(self):

        assert_info = self.tax.delete_tax_rate()
        self.tax.assert_allure_screenshot(assert_info, '删除成功')
