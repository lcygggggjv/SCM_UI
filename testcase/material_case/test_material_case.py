import allure
import pytest

from page_manager.material.material_page import MaterialPage


class TestMaterial:

    mt = None

    @classmethod
    def setup_class(cls):

        cls.mt = MaterialPage()

    @pytest.mark.P0   # po用例
    @allure.testcase(url='', name="新增物料")
    def test_create_material(self):

        assert_info = self.mt.create_material()
        self.mt.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料必填")
    def test_create_material_required(self):

        assert_info = self.mt.create_material_required()
        self.mt.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料唯一性")
    def test_create_material_uniqueness(self):

        assert_info = self.mt.create_material_uniqueness()
        self.mt.assert_allure_screenshot(assert_info, '该物料编码已存在，请重新输入')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增编码长度校验")
    def test_create_code_length(self):

        assert_info = self.mt.create_code_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增名称长度校验")
    def test_create_name_length(self):

        assert_info = self.mt.create_name_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增规格长度校验")
    def test_create_specification_length(self):

        assert_info = self.mt.create_specification_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增型号长度校验")
    def test_create_model_length(self):

        assert_info = self.mt.create_model_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增材质长度校验")
    def test_create_material_quality_length(self):

        assert_info = self.mt.create_material_quality_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增图号长度校验")
    def test_create_figure_no_length(self):

        assert_info = self.mt.create_figure_no_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料2")
    def test_create_material_two(self):

        assert_info = self.mt.create_material_two()
        self.mt.assert_allure_screenshot(assert_info, '新增成功')
