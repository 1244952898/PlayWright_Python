import pytest
import yaml
from playwright.sync_api import sync_playwright


class TestDemo:
    playwright=None
    browser=None
    """
    Test Demo
    """
    @classmethod
    def setup_class(cls):
        """
        测试用例前置条件
        :return:
        """
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=False)
    userData=yaml.safe_load(open("userinfo.yaml","r","utf-8"))
    @pytest.mark.parametrize("username,pwd",[("18710098386","123456"),("18710098386","111111")])
    def test_login(self,username,pwd):
        pass


    def test_updateImg(self):
        pass

    def test_addAddress(self):
        pass

    def test_searchGoods(self):
        pass

    def test_userinfo(self):
        pass

    @classmethod
    def teardown_class(cls):
        """
        测试用例执行完后操作
        :return:
        """
        # cls.context.close()
        cls.browser.close()
        cls.playwright.stop()

# if __name__=="__main__":
#     pytest.main(["-s","example3.py"])