import allure
import pytest

from page_manager.material.material_category_page import MaterialCategoryPage


class TestMaterialCategory:

    cate = None

    def setup_class(self):

        self.cate = MaterialCategoryPage()
        self.cate.goto_material_category()

    @pytest.mark.P0
    @allure.testcase(url="", name='新增一级分类')
    def test_create_material_category(self):

        assert_info = self.cate.create_material_category()
        self.cate.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增分类必填')
    def test_create_category_required(self):

        assert_info = self.cate.create_category_required()
        self.cate.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增分类编码长度校验')
    def test_create_category_code_length(self):

        assert_info = self.cate.create_category_code_length()
        self.cate.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增分类名称长度校验')
    def test_create_category_name_length(self):

        assert_info = self.cate.create_category_name_length()
        self.cate.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增分类名称长度校验')
    def test_create_category_code_uniqueness(self):

        assert_info = self.cate.create_category_code_uniqueness()
        self.cate.assert_allure_screenshot(assert_info, "该分类编码已存在，请重新输入")

    @pytest.mark.P2
    @allure.testcase(url="", name='新增分类2')
    def test_create_two_category(self):

        assert_info = self.cate.create_two_category()
        self.cate.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='编辑分类')
    def test_update_category(self):

        assert_info = self.cate.update_category()
        self.cate.assert_allure_screenshot(assert_info, "编辑成功")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑分类必填')
    def test_update_category_required(self):

        assert_info = self.cate.update_category_required()
        self.cate.assert_allure_screenshot(assert_info, "请填写该必填项")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑分类编码长度校验')
    def test_update_category_code_length(self):

        assert_info = self.cate.update_category_code_length()
        self.cate.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑分类名称长度校验')
    def test_update_category_name_length(self):

        assert_info = self.cate.update_category_name_length()
        self.cate.assert_allure_screenshot(assert_info, "请输入20个字以内的内容")

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑分类名称唯一性校验')
    def test_update_category_uniqueness(self):

        assert_info = self.cate.create_category_code_uniqueness()
        self.cate.assert_allure_screenshot(assert_info, "该分类编码已存在，请重新输入")

    @pytest.mark.P0
    @allure.testcase(url="", name='删除分类')
    def test_delete_category(self):

        assert_info = self.cate.delete_category()
        self.cate.assert_allure_screenshot(assert_info, "删除成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='新增下属分类')
    def test_create_one_category(self):

        assert_info = self.cate.create_one_category()
        self.cate.assert_allure_screenshot(assert_info, "新增成功")

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索分类')
    def test_search_category(self):

        assert_info = self.cate.search_category()
        self.cate.assert_allure_screenshot(assert_info, "999999")
