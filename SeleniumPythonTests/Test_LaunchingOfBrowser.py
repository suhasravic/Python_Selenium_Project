import platform

import pytest

from SeleniumPythonTests import DataDrivenTest as datadriven
from SeleniumPythonTests.BaseClass import BaseClass
from SeleniumPythonTests import LoggerMS as logger


class TestBrowsers(BaseClass):

    def test_browserlaunching(self):
        URL = "https://www.google.com"
        # logger.logger.info("In test_browser launch class")
        # logger.logger.info("hello")
        # logger.logger.info("hello")

        logger.loggingfunction().info("Launcing application --" + URL)
        # my_system = platform.uname()

        # print(f"Operating System: {my_system.system}")
        # print(f"User Name: {my_system.node}")
        # print(f"OS Base version: {my_system.release}")
        # print(f"OS Sub Version: {my_system.version}")
        # print(f"Machine: {my_system.machine}")
        # print(f"Processor: {my_system.processor}")
        # added comment to check the logger
        # self.LaunchApplication(URL)
        # capturedWindowHandle = self.getWindowHandle()
        # print("capturedWindowHandle = ", capturedWindowHandle)
        DataSheet = datadriven.readDataFromExcel("C:\\Users\\USER\\Downloads\\TestDataSheet.xlsx", "Sheet1")
        print("datasheetvalues = ", DataSheet)
        password = datadriven.readRequiredDataFromExcell("C:\\Users\\USER\\Downloads\\TestDataSheet.xlsx", "Sheet1", 0,
                                                         "Password")
        print("password = ", password)
        jsonvalues=datadriven.readDataFromJSONFile("C:\\Users\\USER\\Downloads\\example_1.json")
        print("json values = "+str(jsonvalues))
        jsonvalues1=datadriven.readDataFromJSONFileWithKey("C:\\Users\\USER\\Downloads\\example_1.json","fruit")
        print(jsonvalues1)
        # self.CloseBroser()




