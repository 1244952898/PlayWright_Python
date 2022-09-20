import pytest
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

    @pytest.mark.parametrize("username,pwd",[("18710098386","123456"),("18710098386","111111")])
    def test_login(self,username,pwd):
        """
        登录
        :return:
        """
        page=self.browser.new_page()
        page.goto("https://maomaoyu.com.au/Login/Index")
        page.fill("//input[@id='UserName']", username)
        page.fill("//input[@id='Password']", pwd)
        page.click("//html/body/div[2]/div/div[2]/div[1]/input")
        page.wait_for_timeout(3000)


    def test_updateImg(self):
        """
        更新图片
        :return:
        """
        page = self.browser.new_page()
        page.click("//div[@class='md1200']/div[@class='lginfo pcshow']/a[1]")
        page.click("text=个人资料")
        page.click("//html/body/div[2]/div/div[2]/div[2]/div[1]/input")
        page.locator("//html/body/div[2]/div/div[2]/div[2]/div[1]/input").set_input_files("111.png")
        page.wait_for_timeout(3000)
        page.click("text=保存")

    def test_addAddress(self):
        page = self.browser.new_page()
        page.click("//div[@class='md1200']/div[@class='lginfo pcshow']/a[1]")
        page.wait_for_url("https://maomaoyu.com.au/UserCenter/Index")
        page.click("text=收货人管理")
        page.wait_for_url("https://maomaoyu.com.au/UserCenter/AddressManager")
        page.locator("text=新增收货人").click()
        page.wait_for_url("https://maomaoyu.com.au/UserCenter/EditAddress")
        page.click("[placeholder=\"请输入真实姓名\"]")
        page.fill("[placeholder=\"请输入真实姓名\"]", "收货人姓名")
        page.click("[placeholder=\"请输入手机号码\"]")
        page.fill("[placeholder=\"请输入手机号码\"]", "18710098386")
        page.select_option("#province", "1")
        page.select_option("#city", "1")
        page.select_option("#district", "13")
        page.click("textarea")
        page.fill("textarea", "具体地址")
        page.click("[placeholder=\"请输入邮政编码\"]")
        page.fill("[placeholder=\"请输入邮政编码\"]", "100000")
        page.click("#isDefault")
        page.click("text=保存")
        page.wait_for_url("https://maomaoyu.com.au/UserCenter/AddressManager")

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

if __name__=="__main__":
    pytest.main(["-s","example3.py"])