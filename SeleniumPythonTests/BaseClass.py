import pytest
from selenium import webdriver
from SeleniumPythonTests import LoggerMS as logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from SeleniumPythonTests import DataDrivenTest as datadriven

from SeleniumPythonTests.Oppsmain import Sample


@pytest.mark.usefixtures("browserinvocation")
# @pytest.mark.usefixtures("")
# @pytest.mark.usefixtures("__init__")
class BaseClass:
    # logger.MyLogger.info("from base class")
    # logger.logger.info("chrome browser"
    logger.loggingfunction().info("chrome")


    def ExplicitWaits(self, element):
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            expected_conditions.element_to_be_clickable(self.driver.find_element(By.XPATH, element))).click()

    def LaunchApplication(self, url):
        logger.MyLogger.info("application = "+url)
        self.driver.get(url)

    def getWindowHandle(self):
        return self.driver.current_window_handle

    def CloseBroser(self):
        return self.driver.quit()


