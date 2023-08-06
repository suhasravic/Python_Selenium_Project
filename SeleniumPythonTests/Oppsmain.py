from selenium import webdriver

from POM import HomePage

driver = None


class Sample:
    def __init__(self, request):
        global driver

        BrowserName = request.config.getoption("browser_name")
        if BrowserName == "chrome":
            self.driver = webdriver.Chrome()
        elif BrowserName == "firefox":
            self.driver = webdriver.Firefox()
        elif BrowserName == "":
            print("UNSUPPORTED BROWSER NAME ")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # assigining the local driver to the class driver
        request.cls.self.driver = self.driver
        yield
        self.driver.quit()
