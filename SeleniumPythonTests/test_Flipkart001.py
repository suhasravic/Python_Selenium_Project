import pytest

from POM.HomePage import HomePage
from SeleniumPythonTests.BaseClass import BaseClass
from TestData.Datas import DataSets


class Testflipkart001(BaseClass):
    def test_filpkart(self):
        self.driver.get("https://www.flipkart.com/")
        homepage = HomePage(self.driver)
        cancel="//button[text()='✕']"
        self.ExplicitWaits(cancel)
        # homepage.signInCancel.click()
        homepage.SearchBox().send_keys(getdata["Product"])


    @pytest.fixture(params=DataSets.testdatadetails)
    def getdata(self,request):
        return request.param


