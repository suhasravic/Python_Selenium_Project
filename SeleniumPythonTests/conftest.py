import pytest
import platform
from selenium import webdriver
from SeleniumPythonTests import LoggerMS as logger



driver = None


# driver = any()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
# # def __init__(self, request, driver):
# @pytest.fixture(autouse=True, scope="class")
def browserinvocation(request):
    global driver
    # nonlocal driver
    #         # self.firstvalues = 10
    BrowserName = request.config.getoption("browser_name")
    if BrowserName == "chrome":
        my_system = platform.uname()

        logger.loggingfunction().info(f"Operating System: {my_system.system}")
        logger.loggingfunction().info(f"User Name: {my_system.node}")
        logger.loggingfunction().info(f"OS Base version: {my_system.release}")
        logger.loggingfunction().info(f"OS Sub Version: {my_system.version}")
        logger.loggingfunction().info(f"Machine: {my_system.machine}")
        logger.loggingfunction().info(f"Processor: {my_system.processor}")
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument("--start-maximized")
        chromeoptions.add_argument("--remote-allow-origins=*")
        chromeoptions.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=chromeoptions)
        logger.loggingfunction().info("CHROME Browser Launched")

    elif BrowserName == "firefox":
        driver = webdriver.Firefox()
    elif BrowserName == "":
        print("UNSUPPORTED BROWSER NAME ")
    #
    # logger.info("Window maximized ")
    # driver.maximize_window()
    driver.implicitly_wait(10)
    # return driver

    #
    #         # assigining the local driver to the class driver
    request.cls.driver = driver
    yield
    # logger.loggingfunction().info("Driver.Quit is called")
    driver.quit()


# def getdriver():
#     return driver
# def __init__(self):
#     self.firstnumber = 10


# Report generation
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#
#             file_name = report.nodeid.replace("::", "_") + ".png"
#
#             _capture_screenshot(file_name)
#             file_name.encode(encoding = 'UTF-8')
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)
#
# def handle_write(self):
#     sent = self.send(self.buffer)
#     self.buffer = self.buffer[sent:]
