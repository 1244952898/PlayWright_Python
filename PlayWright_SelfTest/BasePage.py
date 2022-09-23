import allure
import pytest
from playwright.async_api import async_playwright


@allure.feature("PlayWright 测试报告")
class BasePage:

    async def setup_class(self):
        """

        :return:
        """
        self.playwright =await async_playwright().start()
        self.bowser = await self.playwright.chromium.launch(headless=False)

    async def teardown_class(self):
        """

        :return:
        """
        await self.bowser.close()
        await self.playwright.stop()

    async def run_step(self, func, vals):
        """

        :param func:
        :param vals:
        :return:
        """
        await func(*vals)

    async def run_case(self, pocases, page):
        """

        :param pocases:
        :return:
        """
        self.page = page
        allure.dynamic.title(pocases["title"])
        allure.description(pocases["title"])
        cases = pocases["cases"]

        try:
            for case in cases:
                func = self.page.__getattribute__(case["method"])
                params = list(case.values())
                with allure.step(case["name"]):
                    await self.run_step(func, params[2:])
        except Exception:
            allure.attach(self.page.screenshot(), "用例错误图", allure.attachment_type.PNG)
            pytest.fail("Case run fail")

        allure.attach(self.page.screenshot(), "用例成功图", allure.attachment_type.PNG)
