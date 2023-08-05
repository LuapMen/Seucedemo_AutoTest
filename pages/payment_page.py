


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  base.base_class import Base

class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    finish_button = "//*[@id='finish']"


    #Getters
    def get_finish(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.finish_button)))


    #actions

    def click_finish_botton(self):
        self.get_finish().click()
        print("click finish")


    #Methods
    def click_finish(self,):
        self.get_current_url()
        self.click_finish_botton()