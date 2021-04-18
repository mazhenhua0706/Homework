from time import sleep

from selenium.webdriver.common.by import By

from homework3.page.add_department import AddDepartment
from homework3.page.basepage import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def get_list(self):
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = [i.text for i in ele_list]
        # for i in ele_list:
        #     name_list.append(i.text)
        #     print(name_list)
        return name_list

    def goto_add_department(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, ".js_add_sub_party").click()
        return AddDepartment(self.driver)

