from selenium import webdriver
from selenium.common import InvalidArgumentException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from utils.utils_ini import EnvironMent
from hamcrest import assert_that, equal_to
import allure


def get_driver(cls):
    """单例模式，方法级别装饰器函数，放在方法上面 ,然后通过将类以参数传入，
    再判断是否存在实例，没有再创建cls的实例，有直接返回
    """

    instances = {}

    def wrapper(*args, **kwargs):

        if cls not in instances:

            instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        else:
            return instances[cls]

    return wrapper


class BasePage:

    """通过初始化实例driver，ChromeDriverManager插件判断是否需要更新驱动, 下载和浏览器对应版本的驱动,
    实例测试环境对象，获取登录url
    """

    env = EnvironMent()

    @get_driver
    def __init__(self):
        """webdriver.Chrome(ChromeDriverManager().install()) 当前没有115版本的驱动，下载114使用"""

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login_setup()

    def login_setup(self):

        self.driver.maximize_window()
        self.driver.get(self.env.get_env_url())
        self.driver.find_element('xpath', '//input[@name="tenantCode"]').send_keys(self.env.tenantcode())
        self.driver.find_element('xpath', '//input[@name="account"]').send_keys(self.env.account())
        self.driver.find_element('xpath', '//input[@name="password"]').send_keys(self.env.password())
        self.driver.find_element('xpath', "//button[@type='submit']").click()
        self.show_wait_el_clickable(('xpath', "//span[text()='主数据']")).click()
        return self

    def goto_material_category(self):

        self.driver.find_element("xpath", "//span[text()='物料']").click()
        self.driver.find_element("xpath", "//span[text()='物料分类']").click()

    def goto_material_unit(self):

        self.driver.find_element("xpath", "//span[text()='物料']").click()
        self.driver.find_element("xpath", "//span[text()='物料单位']").click()

    def goto_material_signal(self):

        self.driver.find_element("xpath", "//span[text()='物料']").click()
        self.driver.find_element("xpath", "//span[text()='物料信号']").click()

    def goto_material_unit_conversion(self):

        self.driver.find_element("xpath", "//span[text()='物料']").click()
        self.driver.find_element("xpath", "//span[text()='物料单位换算']").click()

    def goto_partner_page(self):

        self.get_element(("xpath", "//span[text()='业务伙伴']")).click()
        self.get_element(("xpath", "//span[text()='业务伙伴信息']")).click()

    def goto_currency_page(self):

        self.get_element(("xpath", "//span[text()='基础信息']")).click()
        self.get_element(("xpath", "//span[text()='币种']")).click()

    def goto_tax_rate_page(self):

        self.get_element(("xpath", "//span[text()='基础信息']")).click()
        self.get_element(("xpath", "//span[text()='税率']")).click()

    def goto_reason_page(self):

        self.get_element(("xpath", "//span[text()='基础信息']")).click()
        self.get_element(("xpath", "//span[text()='原因']")).click()

    def show_wait_el_clickable(self, locator):
        """显性等待，等待元素直到被看到才点击"""
        wait = WebDriverWait(self.driver, timeout=10)

        el = wait.until(expected_conditions.element_to_be_clickable(locator))

        return el

    def get_element(self, locator):
        """定位元素"""
        wait = WebDriverWait(self.driver, timeout=10)
        el = wait.until(expected_conditions.element_to_be_clickable(locator))

        return el

    def action_click(self, el):
        """actionChains"""
        action = ActionChains(self.driver)
        action.click(el).perform()
        return self

    def clicks(self, locator):
        """click点击"""
        el = self.driver.find_element(*locator)
        try:
            el.click()

        except InvalidArgumentException as e:  # try,click点击不了，捕获异常，满足InvalidArgumentException错误类型
            # 通过action方法点击
            ActionChains(self.driver).click(el).perform()  # 初始化action对象
        return self

    def send_keys(self, locator, word):
        """输入"""
        el = self.get_element(locator)

        try:
            el.send_keys(word)
        except:
            ActionChains(self.driver).send_keys(el, word).perform()
            # 先移动定位光标元素，再输入内容
        return self

    def get_alert(self, locator):

        el = self.show_wait_el_clickable(locator)

        return el.text

    def clear(self, locator):
        """清空"""
        el = self.get_element(locator)
        el.clear()
        return self

    def assert_allure_screenshot(self, actual, expected):
        """断言失败就截图，输出再报告里"""

        try:
            assert_that(actual, equal_to(expected))

        except AssertionError as e:
            img = self.driver.get_screenshot_as_png()
            allure.attach(img, name='用例失败截图', attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"断言失败：预期结果：{expected} ,!= 实际结果：{actual}") from e

    def visibility_el(self, locator):
        """这个显性等待判断元素是否被看到，能看到true，否则false"""
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            wait.until(expected_conditions.visibility_of_element_located(locator))
            return True
        except NoSuchElementException:

            return False

    def is_el_present(self, locator):
        # 判断元素是否存在，存在返回true，不存在返回false，不会报错
        try:

            self.driver.find_element(*locator)
            return True

        except NoSuchElementException:

            return False

    def move_to_el(self, locator):
        """移动鼠标到元素处"""

        el = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(el).perform()
        return self

    def double_click_delete(self, element):
        # 双击删除
        el = self.driver.find_element(By.XPATH, element)
        ActionChains(self.driver).double_click(el).perform()
        el.send_keys(7 * Keys.BACK_SPACE)
        return el

    def scroll_el(self, locator):
        """通过定位元素来进行，水平，垂直控制滚动条，加上时间等待"""
        # 1： self.driver.execute_script("window.scrollTo(0, 1000)")
        # js的window.scrollTo()方法    window.scrollTo(x,y) 通过坐标(x,y)进行滑动  不行
        # 2：设置滚动条位置
        # execute_script(“document.documentElement.scrollTop= 位置”)
        # driver.execute_script("document.documentElement.scrollTop=10000")  不行、

        el = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView()", el)
        return self

    def all_select_delete_mac(self, locator):
        #  command +a  mac
        el = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).key_down(Keys.COMMAND)   # # 先按COMMAND 再按a
        ActionChains(self.driver).send_keys("a").key_up(Keys.COMMAND).perform()   # 后面要加perform
        el.send_keys(7 * Keys.BACK_SPACE)
        return el

    def all_select_delete_win(self, locator):
        #  control +a   win
        el = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).key_down(Keys.CONTROL)   # # 先按control 再按a
        ActionChains(self.driver).send_keys("a").key_up(Keys.CONTROL).perform()   # 后面要加perform
        el.send_keys(7 * Keys.BACK_SPACE)
        return el
