from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self.driver = ""
        if driver is None:
            # 使用浏览器复用模式
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get("https://work.weixin.qq.com/")
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
            self.driver.implicitly_wait(3)
        if self._base_url != "":
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(3)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)


