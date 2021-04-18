from homework3.page.main import Main1



class TestAddMember:
    def test_add_member(self):
        self.main = Main1()
        res = self.main.goto_add_member().add_member().get_list()
        assert "德玛西亚" in res