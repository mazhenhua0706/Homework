from homework3.page.main import Main1
from homework3.page.contact_page import ContactPage


class TestAddDepartment:
    def test_add_department(self):
        self.main = Main1()
        self.main.goto_contact().goto_add_department().add_department()

