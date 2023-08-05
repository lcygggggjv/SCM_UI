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
    @allure.testcase(url='', name="新增物料类型固定选项校验")
    def test_create_material_type_verification(self):

        assert_info = self.mt.create_material_type_verification()
        self.mt.assert_allure_screenshot(assert_info, True)

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料2")
    def test_create_material_two(self):

        assert_info = self.mt.create_material_two()
        self.mt.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P0
    @allure.testcase(url='', name="编辑物料")
    def test_update_material(self):

        assert_info = self.mt.update_material()
        self.mt.assert_allure_screenshot(assert_info, '编辑成功')

    @pytest.mark.P0
    @allure.testcase(url='', name="编辑物料必填")
    def test_update_material_required(self):

        assert_info = self.mt.update_material_required()
        self.mt.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑名称长度校验")
    def test_update_specification_length(self):

        assert_info = self.mt.update_specification_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑规格长度校验")
    def test_update_specification_length(self):

        assert_info = self.mt.update_specification_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑型号长度校验")
    def test_update_model_length(self):

        assert_info = self.mt.update_model_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑材质长度校验")
    def test_update_material_quality_length(self):

        assert_info = self.mt.update_material_quality_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑图号长度校验")
    def test_update_figure_no_length(self):

        assert_info = self.mt.update_figure_no_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑物料类型固定选项校验")
    def test_update_material_type_verification(self):

        assert_info = self.mt.update_material_type_verification()
        self.mt.assert_allure_screenshot(assert_info, True)

    @pytest.mark.P0
    @allure.testcase(url='', name="复制物料")
    def test_copy_material(self):

        assert_info = self.mt.copy_material()
        self.mt.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制物料必填")
    def test_copy_material_required(self):

        assert_info = self.mt.copy_material_required()
        self.mt.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制编码长度校验")
    def test_copy_code_length(self):

        assert_info = self.mt.copy_code_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制名称长度校验")
    def test_copy_name_length(self):

        assert_info = self.mt.copy_name_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制规格长度校验")
    def test_copy_specification_length(self):

        assert_info = self.mt.copy_specification_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制型号长度校验")
    def test_copy_model_length(self):

        assert_info = self.mt.copy_model_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制材质长度校验")
    def test_copy_material_quality_length(self):

        assert_info = self.mt.copy_material_quality_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制图号长度校验")
    def test_copy_figure_no_length(self):

        assert_info = self.mt.copy_figure_no_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="复制物料类型固定选项校验")
    def test_copy_material_type_verification(self):

        assert_info = self.mt.copy_material_type_verification()
        self.mt.assert_allure_screenshot(assert_info, True)

    @pytest.mark.P2
    @allure.testcase(url='', name="查看物料详情页面")
    def test_goto_detail_verification(self):

        assert_info = self.mt.goto_detail_verification()
        self.mt.assert_allure_screenshot(assert_info, '基础信息')

    @pytest.mark.P0
    @allure.testcase(url='', name="详情编辑物料")
    def test_detail_update_material(self):

        assert_info = self.mt.detail_update_material()
        self.mt.assert_allure_screenshot(assert_info, '编辑成功')

    @pytest.mark.P0
    @allure.testcase(url='', name="详情编辑物料必填")
    def test_detail_update_material_required(self):

        assert_info = self.mt.detail_update_material_required()
        self.mt.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情编辑名称长度校验")
    def test_detail_update_name_length(self):

        assert_info = self.mt.detail_update_name_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情编辑规格长度校验")
    def test_detail_update_specification_length(self):

        assert_info = self.mt.detail_update_specification_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情编辑型号长度校验")
    def test_detail_update_model_length(self):

        assert_info = self.mt.detail_update_model_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情编辑材质长度校验")
    def test_detail_update_material_quality_length(self):

        assert_info = self.mt.detail_update_material_quality_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情编辑图号长度校验")
    def test_detail_update_figure_no_length(self):

        assert_info = self.mt.detail_update_figure_no_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情编辑物料类型固定选项校验")
    def test_detail_update_material_type_verification(self):

        assert_info = self.mt.detail_update_material_type_verification()
        self.mt.assert_allure_screenshot(assert_info, True)

    @pytest.mark.P0
    @allure.testcase(url='', name="详情复制物料")
    def test_detail_copy_material(self):

        assert_info = self.mt.detail_copy_material()
        self.mt.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制物料必填")
    def test_detail_copy_material_required(self):

        assert_info = self.mt.detail_copy_material_required()
        self.mt.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制编码长度校验")
    def test_detail_copy_code_length(self):

        assert_info = self.mt.detail_copy_code_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制名称长度校验")
    def test_detail_copy_name_length(self):

        assert_info = self.mt.detail_copy_name_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制规格长度校验")
    def test_detail_copy_specification_length(self):

        assert_info = self.mt.detail_copy_specification_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制型号长度校验")
    def test_detail_copy_model_length(self):

        assert_info = self.mt.detail_copy_model_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制材质长度校验")
    def test_detail_copy_material_quality_length(self):

        assert_info = self.mt.detail_copy_material_quality_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制图号长度校验")
    def test_detail_copy_figure_no_length(self):

        assert_info = self.mt.detail_copy_figure_no_length()
        self.mt.assert_allure_screenshot(assert_info, '请输入60个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="详情复制物料类型固定选项校验")
    def test_detail_copy_material_type_verification(self):

        assert_info = self.mt.detail_copy_material_type_verification()
        self.mt.assert_allure_screenshot(assert_info, True)

    @pytest.mark.P0
    @allure.testcase(url='', name="详情删除物料")
    def test_detail_delete(self):

        assert_info = self.mt.detail_delete()
        self.mt.assert_allure_screenshot(assert_info, "删除成功")
