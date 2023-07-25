from page_manager.basepage import BasePage


class MaterialPage(BasePage):

    def create_material(self):
        """新增物料"""
        self.get_element(("xpath", "//button[text()='新增物料']")).click()
        self.get_element(("xpath", "//input[@name='no'][@placeholder='请输入']")).send_keys('9568')
        self.get_element(("xpath", "//input[@name='name'][@placeholder='请输入']")).send_keys('xxx')
        self.get_element(("xpath", '//input[@id=":rf:"][@placeholder="请选择"]')).click()
        self.get_element(("xpath", '//li[@role="option"][@tabindex="-1"]')).click()
        self.get_element(("xpath", "//button[text()='确定']")).click()

        assert_info = self.get_alert(("xpath", '//div[text()="新增成功"]'))

        return assert_info

