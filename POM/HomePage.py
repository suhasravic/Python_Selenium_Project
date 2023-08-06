from selenium.webdriver.common.by import By


class HomePage:
    # creation of constructor
    def __init__(self,driver):
        self.driver = driver
    searchBox = (By.NAME,"q")
    signInCancel=(By.XPATH,"//button[text()='✕']")

    def SearchBox(self):
        return self.driver.find_element(*HomePage.searchBox)
    def SignInCancelButton(self):
        return self.driver.find_element(*HomePage.signInCancel)
