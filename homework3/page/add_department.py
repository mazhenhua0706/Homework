from time import sleep

from selenium.webdriver.common.by import By

from homework3.page.basepage import BasePage


class AddDepartment(BasePage):
    def add_department(self):
        from homework3.page.contact_page import ContactPage
        self.find(By.NAME, "name").send_keys("第一部门")
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return ContactPage(self.driver)

