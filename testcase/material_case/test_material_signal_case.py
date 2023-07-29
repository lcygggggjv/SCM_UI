import allure
import pytest

from page_manager.material.material_signal import MaterialSignalPage


class TestMaterialSignal:

    signal = None

    @classmethod
    def setup_class(cls):

        cls.signal = MaterialSignalPage()
        cls.signal.goto_material_signal()

    @pytest.mark.P0   # po用例
    @allure.testcase(url='', name="新增物料信号")
    def test_create_signal(self):

        assert_info = self.signal.create_signal()
        self.signal.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料信号必填")
    def test_create_signal_required(self):

        assert_info = self.signal.create_signal_required()
        self.signal.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料信号编码长度校验")
    def test_create_signal_code_length(self):

        assert_info = self.signal.create_signal_code_length()
        self.signal.assert_allure_screenshot(assert_info, '请输入5个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料信号名称长度校验")
    def test_create_signal_name_length(self):

        assert_info = self.signal.create_signal_name_length()
        self.signal.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料信号编码唯一性校验")
    def test_create_signal_uniqueness(self):

        assert_info = self.signal.create_signal_uniqueness()
        self.signal.assert_allure_screenshot(assert_info, '该信号编码已存在，请重新输入')

    @pytest.mark.P2
    @allure.testcase(url='', name="新增物料信号2")
    def test_create_signal_two(self):

        assert_info = self.signal.create_signal_two()
        self.signal.assert_allure_screenshot(assert_info, '新增成功')

    @pytest.mark.P0
    @allure.testcase(url='', name="编辑物料信号")
    def test_update_signal(self):

        assert_info = self.signal.update_signal()
        self.signal.assert_allure_screenshot(assert_info, '编辑成功')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑物料信号描述必填")
    def test_update_signal_required(self):

        assert_info = self.signal.update_signal_required()
        self.signal.assert_allure_screenshot(assert_info, '请填写该必填项')

    @pytest.mark.P2
    @allure.testcase(url='', name="编辑物料信号名称长度校验")
    def test_update_signal_name_length(self):

        assert_info = self.signal.update_signal_name_length()
        self.signal.assert_allure_screenshot(assert_info, '请输入20个字以内的内容')

    @pytest.mark.P2
    @allure.testcase(url="", name='编辑物料信号名称disabled校验')
    def test_update_signal_disable(self):

        assert_info = self.signal.update_signal_disable()
        self.signal.assert_allure_screenshot(assert_info, 'true')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索信号编码')
    def test_search_code(self):

        assert_info = self.signal.search_signal_code()
        self.signal.assert_allure_screenshot(assert_info, '99999')

    @pytest.mark.P2
    @allure.testcase(url="", name='重置搜索信号编码')
    def test_resetting_search_code(self):

        assert_info = self.signal.signal_resetting_search()
        self.signal.assert_allure_screenshot(assert_info, '')

    @pytest.mark.P0
    @allure.testcase(url="", name='搜索信号描述')
    def test_search_name(self):

        assert_info = self.signal.search_signal_name()
        self.signal.assert_allure_screenshot(assert_info, '88888')

    @pytest.mark.P0
    @allure.testcase(url="", name='删除物料信号')
    def test_delete_signal(self):

        assert_info = self.signal.delete_signal()
        self.signal.assert_allure_screenshot(assert_info, '删除成功')

    @pytest.mark.P2
    @allure.testcase(url="", name='批量删除物料信号')
    def test_batch_delete_signal(self):

        assert_info = self.signal.batch_delete_signal()
        self.signal.assert_allure_screenshot(assert_info, '删除成功')
