import allure
import pytest
import yaml
from playwright.sync_api import sync_playwright

f=open("TestCase.yaml","r",encoding="utf-8")
case_file=yaml.safe_load(f)
print(case_file)

@allure.feature("PlayWright 测试报告")
class Test_Web:
    def run_step(self,func,val):
        """
        测试步骤
        :param func:
        :param val:
        :return:
        """
        func(*val)

    def run_case(self,POCases):
        allure.dynamic.title(POCases["title"])
        allure.description(POCases["title"])
        cases=POCases["cases"]
        try:
            for case in cases:
                func=self.page.__getattribute__(case["method"])
                params=list(case.values())
                with allure.step(case["name"]):
                    self.run_step(func,params[2:])
        except Exception:
            allure.attach(self.page.screenshot(),"用例错误图",allure.attachment_type.PNG)
            pytest.fail("Case run fail")
        allure.attach(self.page.screenshot(), "用例成功图", allure.attachment_type.PNG)

    def setup_class(self):
        self.playwright=sync_playwright().start()
        self.bowser=self.playwright.chromium.launch(headless=False)
        self.page=self.bowser.new_page()

    def teardown_class(self):
        self.bowser.close()
        self.playwright.stop()

    @allure.story("登录story")
    @pytest.mark.parametrize("POCases",case_file["loginpage"])
    def test_login(self,POCases):
        self.run_case(POCases)
        self.page.wait_for_timeout(3000)