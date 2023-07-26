import allure
import pytest

from page_manager.material.materialpage import MaterialPage


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

