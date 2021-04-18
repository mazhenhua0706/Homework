from selenium.webdriver.common.by import By
from homework3.page.basepage import BasePage
from homework3.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self):
        # 填写信息
        self.driver.find_element(By.ID, "username").send_keys("德玛西亚")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("123456")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13018063698")
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()

        return ContactPage(self.driver)

    def goto_contact(self):
        pass
