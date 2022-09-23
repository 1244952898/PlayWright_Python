import allure
import pytest
from ReadYaml import ReadYaml
from PlayWright_SelfTest.BasePage import BasePage

@allure.feature("PlayWright 测试报告")
class test_LoginPage(BasePage):

    @allure.story("登录story")
    async def test_login(self):
        POCases=ReadYaml.readyamlfile("./tools/test.yaml")
        await self.run_case(POCases)
        self.page.wait_for_timeout(3000)
