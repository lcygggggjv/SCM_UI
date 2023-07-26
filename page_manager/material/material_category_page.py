
from page_manager.basepage import BasePage
from common.mock import Mock


class MaterialCategoryPage(BasePage):

    def create_material_category(self):
        """新增一级分类"""

        self.get_element(('xpath', "//button[text()='新增一级分类']")).click()
        self.get_element(("xpath", "//input[@name='no']")).send_keys(Mock.faker_pystr())
        self.get_element(("xpath", "//input[@name='name']")).send_keys(Mock.faker_pystr())
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='新增成功']"))

        return assert_info

    def create_category_required(self):
        """新增分类必填"""

        self.get_element(('xpath', "//button[text()='新增一级分类']")).click()
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))

        return assert_info

    def create_category_code_length(self):
        """新增分类，编码长度校验"""

        self.get_element(('xpath', "//button[text()='新增一级分类']")).click()
        self.get_element(("xpath", "//input[@name='no']")).send_keys(Mock.faker_pystr_21())
        self.get_element(("xpath", "//input[@name='name']")).send_keys(Mock.faker_pystr())
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))

        return assert_info

    def create_category_name_length(self):
        """新增分类，分类长度校验"""

        self.get_element(('xpath', "//button[text()='新增一级分类']")).click()
        self.get_element(("xpath", "//input[@name='no']")).send_keys(Mock.faker_pystr())
        self.get_element(("xpath", "//input[@name='name']")).send_keys(Mock.faker_pystr_21())
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))

        return assert_info

    def create_category_code_uniqueness(self):
        """新增分类，编码唯一性校验"""

        self.get_element(('xpath', "//button[text()='新增一级分类']")).click()
        self.get_element(("xpath", "//input[@name='no']")).send_keys('2312')
        self.get_element(("xpath", "//input[@name='name']")).send_keys(Mock.faker_pystr())
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='该分类编码已存在，请重新输入']"))

        return assert_info

    def update_category(self):
        """编辑物料分类"""

        self.get_element(("xpath", '(//div[@style="position: relative;"]//div[@role="button"])[1]')).click()
        self.get_element(("xpath", '(//button[@class="MuiButtonBase-root '
                                   'MuiIconButton-root MuiIconButton-sizeSmall css-v765fw"])[4]')).click()
        self.get_element(("xpath", "(//ul//li[text()='编辑'])[1]")).click()
        self.get_element(("xpath", "//input[@name='no']")).clear()
        self.get_element(("xpath", "//input[@name='name']")).clear()
        self.get_element(("xpath", "//input[@name='no']")).send_keys(Mock.faker_pystr())
        self.get_element(("xpath", "//input[@name='name']")).send_keys(Mock.faker_pystr())
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='编辑成功']"))

        return assert_info

    def update_category_required(self):
        """编辑物料分类 必填"""

        self.get_element(("xpath", '(//div[@style="position: relative;"]//div[@role="button"])[1]')).click()
        self.get_element(("xpath", '(//button[@class="MuiButtonBase-root '
                                   'MuiIconButton-root MuiIconButton-sizeSmall css-v765fw"])[4]')).click()
        self.get_element(("xpath", "(//ul//li[text()='编辑'])[1]")).click()
        self.get_element(("xpath", "//input[@name='no']")).clear()
        self.get_element(("xpath", "//input[@name='name']")).clear()
        # self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='请填写该必填项']"))

        return assert_info

    def update_category_code_length(self):
        """编辑物料分类 编码长度校验"""

        self.get_element(("xpath", '(//div[@style="position: relative;"]//div[@role="button"])[1]')).click()
        self.get_element(("xpath", '(//button[@class="MuiButtonBase-root '
                                   'MuiIconButton-root MuiIconButton-sizeSmall css-v765fw"])[4]')).click()
        self.get_element(("xpath", "(//ul//li[text()='编辑'])[1]")).click()
        self.get_element(("xpath", "//input[@name='no']")).clear()
        self.get_element(("xpath", "//input[@name='no']")).send_keys(Mock.faker_pystr_21())
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))

        return assert_info

    def update_category_name_length(self):
        """编辑物料分类 名称长度校验"""

        self.get_element(("xpath", '(//div[@style="position: relative;"]//div[@role="button"])[1]')).click()
        self.get_element(("xpath", '(//button[@class="MuiButtonBase-root '
                                   'MuiIconButton-root MuiIconButton-sizeSmall css-v765fw"])[4]')).click()
        self.get_element(("xpath", "(//ul//li[text()='编辑'])[1]")).click()
        self.get_element(("xpath", "//input[@name='name']")).clear()
        self.get_element(("xpath", "//input[@name='name']")).send_keys(Mock.faker_pystr_21())
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='请输入20个字以内的内容']"))

        return assert_info

    def update_category_uniqueness(self):
        """编辑物料分类 编码唯一性校验"""

        self.get_element(("xpath", '(//div[@style="position: relative;"]//div[@role="button"])[1]')).click()
        self.get_element(("xpath", '(//button[@class="MuiButtonBase-root '
                                   'MuiIconButton-root MuiIconButton-sizeSmall css-v765fw"])[4]')).click()
        self.get_element(("xpath", "(//ul//li[text()='编辑'])[1]")).click()
        self.get_element(("xpath", "//input[@name='no']")).clear()
        self.get_element(("xpath", "//input[@name='no']")).send_keys('2312')
        self.get_element(("xpath", "//button[text()='确定']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='该分类编码已存在，请重新输入']"))

        return assert_info

    def delete_category(self):
        """删除物料"""
        self.get_element(("xpath", '(//div[@style="position: relative;"]//div[@role="button"])[1]')).click()
        self.get_element(("xpath", '(//button[@class="MuiButtonBase-root '
                                   'MuiIconButton-root MuiIconButton-sizeSmall css-v765fw"])[4]')).click()
        self.get_element(("xpath", "(//ul//li[text()='删除'])[1]")).click()
        self.get_element(("xpath", "//button[text()='删除']")).click()
        assert_info = self.get_alert(("xpath", "//div[text()='删除成功']"))

        return assert_info
