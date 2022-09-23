import os

import pytest

import tools.ReadYaml

if __name__ == '__main__':

    # playwright = sync_playwright().start()
    # bowser = playwright.chromium.launch(headless=False)
    # # Open new page
    # page =  bowser.new_page()
    # print(dir(page))
    print(tools.ReadYaml.ReadYaml.readyamlfile("./tools/test.yaml"))
    os.system("rd /s/q temp")
    os.system("rd /s/q report")
    pytest.main(["-s","./Login/test_LoginPage.py","--alluredir","./temp"])
    os.system("allure generate ./temp -o ./report --clean")