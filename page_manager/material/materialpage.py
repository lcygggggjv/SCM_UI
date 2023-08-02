from page_manager.basepage import BasePage
from common.mock import Mock


class MaterialPage(BasePage):

    def create_material(self):
        """新增物料"""

        self.driver.find_element("xpath", "//button[text()='新增物料']").click()
        self.driver.find_element("xpath", "//input[@name='no'][@placeholder='请输入']").send_keys(Mock().faker_pystr())
        self.driver.find_element("xpath", "//input[@name='name'][@placeholder='请输入']").send_keys(Mock().faker_pystr())
        self.driver.find_element("xpath", '//div[@name="inventoryUnit"]//input').click()
        self.driver.find_element("xpath", '//li[@role="option"][@tabindex="-1"]').click()
        self.driver.find_element("xpath", "//button[text()='确定']").click()
        assert_info = self.get_alert(("xpath", '//div[text()="新增成功"]'))
        return assert_info

