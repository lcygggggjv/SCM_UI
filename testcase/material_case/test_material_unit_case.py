import allure
import pytest
from page_manager.material.material_unit_page import MaterialUnitPage


class TestMaterialUint:

    unit = None

    def setup_class(self):

        self.unit = MaterialUnitPage()
        self.unit.goto_material_unit()

    @pytest.mark.P0
    @allure.testcase(url="", name='新增单位')
    def test_create_unit(self):

        assert_info = self.unit.create_unit()
        self.unit.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位必填')
    def test_create_unit_required(self):

        assert_info = self.unit.create_unit_required()
        self.unit.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位名称长度校验')
    def test_create_unit_name_length(self):

        assert_info = self.unit.create_unit_name_length()
        self.unit.assert_allure_screenshot(assert_info, "请输入5个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位简称长度校验')
    def test_create_unit_jc_length(self):

        assert_info = self.unit.create_unit_jc_length()
        self.unit.assert_allure_screenshot(assert_info, "请输入5个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位备注长度校验')
    def test_create_unit_remark_length(self):

        assert_info = self.unit.create_unit_remark_length()
        self.unit.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位名称唯一性校验')
    def test_create_unit_uniqueness(self):

        assert_info = self.unit.create_unit_uniqueness()
        self.unit.assert_allure_screenshot(assert_info, "该单位名称已存在，请重新输入")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位2')
    def test_create_unit_two(self):

        assert_info = self.unit.create_unit_two()
        self.unit.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='编辑单位')
    def test_update_unit(self):

        assert_info = self.unit.update_unit()
        self.unit.assert_allure_screenshot(assert_info, "编辑成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑单位简称长度校验')
    def test_update_unit_jc_length(self):

        assert_info = self.unit.update_unit_jc_length()
        self.unit.assert_allure_screenshot(assert_info, "请输入5个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位备注长度校验')
    def test_update_unit_remark_length(self):

        assert_info = self.unit.update_unit_remark_length()
        self.unit.assert_allure_screenshot(assert_info, "请输入60个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增单位名称disabled校验')
    def test_update_unit_disable(self):

        assert_info = self.unit.update_unit_disable()
        self.unit.assert_allure_screenshot(assert_info, 'true')

    @pytest.mark.P0
    @allure.testcase(url="", name='删除单位')
    def test_delete_unit(self):

        assert_info = self.unit.delete_unit()
        self.unit.assert_allure_screenshot(assert_info, '删除成功')

    @pytest.mark.P2
    @allure.testcase(url="", name='批量删除单位')
    def test_batch_delete_unit(self):

        assert_info = self.unit.batch_delete_unit()
        self.unit.assert_allure_screenshot(assert_info, '删除成功')
