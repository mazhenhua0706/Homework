from selenium.webdriver.common.by import By

from homework3.page.add_member_page import AddMemberPage
from homework3.page.basepage import BasePage
from homework3.page.contact_page import ContactPage
from homework3.page.login import Login
from homework3.page.register import Register


class Main(BasePage):
    # 点击注册
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self.driver)


class Main1(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)
