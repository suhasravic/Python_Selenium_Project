from SeleniumPythonTests.BaseClass import BaseClass


class methodsinvocation(BaseClass):
    def __init__(self,driver,URL):
        self.driver = driver
    UrL = ( "https://www.google.com")
        # getmethodvalue=self.driver.get("https://www.google.com")

    def gm(self):
        return self.driver.get(methodsinvocation.URL)
        # objtt = self.driver.get(str(url))
        # return url
