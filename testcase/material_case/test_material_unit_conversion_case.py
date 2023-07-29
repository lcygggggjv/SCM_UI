import allure
import pytest

from page_manager.material.material_unit_conversion_page import MaterialUnitConversionPage


class TestMaterialSignal:

    conversion = None

    @classmethod
    def setup_class(cls):

        cls.conversion = MaterialUnitConversionPage()
        cls.conversion.goto_material_unit_conversion()

    @pytest.mark.P0   # po用例
    @allure.testcase(url='', name="新增物料信号")
    def test_create_conversion(self):

        assert_info = self.conversion.create_unit_conversion()
        self.conversion.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料信号必填")
    def test_create_conversion_required(self):

        assert_info = self.conversion.create_conversion_required()
        self.conversion.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增单位换算物料不存在校验")
    def test_create_signal_code_absent(self):

        assert_info = self.conversion.create_conversion_code_absent()
        self.conversion.assert_allure_screenshot(assert_info, '该物料编码不存在，请重新输入')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增单位换算，单位不与本相同")
    def test_create_conversion_different(self):

        assert_info = self.conversion.create_conversion_different()
        self.conversion.assert_allure_screenshot(assert_info, '“基本单位”不得与“目标单位”相同')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增单位系数，小数位数3位")
    def test_create_conversion_coefficient(self):

        assert_info = self.conversion.create_conversion_coefficient()
        self.conversion.assert_allure_screenshot(assert_info, '小数最多保留小数点后3位')

    @pytest.mark.P0
    @allure.testcase(url='', name="新增置灰属性")
    def test_create_conversion_disable_verification(self):

        assert_info = self.conversion.create_conversion_disable_verification()
        self.conversion.assert_allure_screenshot(assert_info, True)

    @pytest.mark.P2
    @allure.testcase(url='', name="新增单位换算2")
    def test_create_conversion_two(self):

        assert_info = self.conversion.create_conversion_two()
        self.conversion.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索基本单位')
    def test_search_conversion_unit(self):

        assert_info = self.conversion.search_conversion_unit()
        self.conversion.assert_allure_screenshot(assert_info, '99999')

    @pytest.mark.P2
    @allure.testcase(url="", name='重置搜索基本单位')
    def test_resetting_search_unit(self):

        assert_info = self.conversion.conversion_resetting_search()
        self.conversion.assert_allure_screenshot(assert_info, '')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索目标单位')
    def test_search_conversion_material_code(self):

        assert_info = self.conversion.search_conversion_target_unit()
        self.conversion.assert_allure_screenshot(assert_info, '88888')

    @pytest.mark.P2
    @allure.testcase(url="", name='搜索物料编码')
    def test_search_conversion_material_code(self):

        assert_info = self.conversion.search_conversion_material_code()
        self.conversion.assert_allure_screenshot(assert_info, '99999')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索物料名称')
    def test_search_conversion_material_name(self):

        assert_info = self.conversion.search_conversion_material_name()
        self.conversion.assert_allure_screenshot(assert_info, '88888')

    @pytest.mark.P0
    @allure.testcase(url="", name='删除物料单位换算')
    def test_delete_conversion(self):

        assert_info = self.conversion.delete_conversion()
        self.conversion.assert_allure_screenshot(assert_info, '删除成功')

    @pytest.mark.P2
    @allure.testcase(url="", name='批量删除物料单位换算')
    def test_batch_delete_conversion(self):

        assert_info = self.conversion.batch_delete_conversion()
        self.conversion.assert_allure_screenshot(assert_info, '删除成功')
