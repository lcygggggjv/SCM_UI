from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from utils.utils_ini import EnvironMent

def get_driver(cls):
    """单例模式，装饰器函数,通过将类以参数传入，
    再判断是否存在实例，没有再进行实例，有直接返回
    """

    driver = {}

    def wrapper(*args, **kwargs):

        if cls not in driver:

            driver[cls] = cls(*args, **kwargs)

        else:
            return driver[cls]

    return wrapper



class BasePage:

    """通过初始化实例driver，ChromeDriverManager插件判断是否需要更新驱动,
    实例测试环境对象，获取登录url
    """

    env = EnvironMent()

    def __init__(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.login_setup()


    def login_setup(self):

        self.driver.maximize_window()
        self.driver.get(self.env.get_env_url())
        self.driver.find_element('xpath', "tenantCode").send_keys(self.env.tenantcode())
        self.driver.find_element('xpath', "account").send_keys(self.env.account)
        self.driver.find_element('xpath', "password").send_keys(self.env.password)
        self.driver.find_element('xpath', "//button[@type='submit']").click()
        self.show_wait_el_clickable(('xpath', "(//button[@type='button'])[1]"))
        self.driver.find_element('xpath', "(//button[@type='button'])[1]").click()
        self.show_wait_el_clickable(('xpath', '//p[text()="设备资产管理"]'))
        self.driver.find_element('xpath', '//p[text()="设备资产管理"]').click()

        return self


    def show_wait_el_clickable(self, locator):
        """显性等待，等待元素直到被看到才点击"""
        wait = WebDriverWait(self.driver, timeout=10)

        el = wait.until(expected_conditions.element_to_be_clickable(locator))

        return el
