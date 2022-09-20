import asyncio
from playwright.async_api import Playwright, async_playwright, expect
async def run(playwright: Playwright) -> None:
    """
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    :param playwright:
    :return:
    """
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    # await page.goto("https://maomaoyu.com.au/Login/Index")
    # # Click text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder="请输入手机号"]
    # await page.locator("text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder=\"请输入手机号\"]").click()
    # # Fill text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder="请输入手机号"]
    # await page.locator("text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder=\"请输入手机号\"]").fill("18710098386")
    # # Click text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder="请输入密码"]
    # await page.locator("text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder=\"请输入密码\"]").click()
    # # Fill text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder="请输入密码"]
    # await page.locator("text=使用验证码登录 +86 +61 忘记密码？ 登录 >> [placeholder=\"请输入密码\"]").fill("123456")
    # # Click text=使用验证码登录 +86 +61 忘记密码？ 登录 >> input[type="button"]
    # await page.locator("text=使用验证码登录 +86 +61 忘记密码？ 登录 >> input[type=\"button\"]").click()
    # await page.wait_for_url("https://maomaoyu.com.au/Home/Index")
    # box= await page.locator("text=使用验证码登录 +86 +61 忘记密码？ 登录 >> input[type=\"button\"]").bounding_box()
    # print(box["x"] , box["width"])

    await page.goto("https://maomaoyu.com.au/Login/Index")
    await page.fill("//input[@id='UserName']","18710098386")
    await page.fill("//input[@id='Password']","123456")
    await page.click("//html/body/div[2]/div/div[2]/div[1]/input")

    # await page.click("//div[@class='md1200']/div[@class='lginfo pcshow']/a[1]")
    # await page.click("text=个人资料")
    # await page.click("//html/body/div[2]/div/div[2]/div[2]/div[1]/input")
    # await page.locator("//html/body/div[2]/div/div[2]/div[2]/div[1]/input").set_input_files("111.png")
    # await page.wait_for_timeout(3000)
    # await page.click("text=保存")

    # await page.click("//div[@class='md1200']/div[@class='lginfo pcshow']/a[1]")
    # await page.wait_for_url("https://maomaoyu.com.au/UserCenter/Index")
    # await page.click("text=收货人管理")
    # await page.wait_for_url("https://maomaoyu.com.au/UserCenter/AddressManager")
    # await page.locator("text=新增收货人").click()
    # await page.wait_for_url("https://maomaoyu.com.au/UserCenter/EditAddress")
    # await page.click("[placeholder=\"请输入真实姓名\"]")
    # await page.fill("[placeholder=\"请输入真实姓名\"]", "收货人姓名")
    # await page.click("[placeholder=\"请输入手机号码\"]")
    # await page.fill("[placeholder=\"请输入手机号码\"]", "18710098386")
    # await page.select_option("#province", "1")
    # await page.select_option("#city", "1")
    # await page.select_option("#district", "13")
    # await page.click("textarea")
    # await page.fill("textarea", "具体地址")
    # await page.click("[placeholder=\"请输入邮政编码\"]")
    # await page.fill("[placeholder=\"请输入邮政编码\"]", "100000")
    # await page.click("#isDefault")
    # await page.click("text=保存")
    # await page.wait_for_url("https://maomaoyu.com.au/UserCenter/AddressManager")

    # Click [placeholder="搜索商品"]
    await page.click("#keyWord")
    # Fill [placeholder="搜索商品"]
    await page.fill("#keyWord","苹果")
    # Click .searchbtn
    await page.click(".searchbtn")
    #await page.wait_for_url("https://maomaoyu.com.au/goods/index")
    await page.wait_for_timeout(1000)

    goods=await page.query_selector_all("//ul[@id='datalist']/li/div[@class='infobox']/p")
    for good in goods:
        print(await good.text_content())

    await page.click()

    await page.wait_for_timeout(3000)
    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
