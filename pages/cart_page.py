


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    checkout = "//*[@id='checkout']"



    #Getters
    def get_checkout(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.checkout)))


    #actions

    def click_checkout(self):
        self.get_checkout().click()
        print("click checkout")


    #Methods
    def select_checkout(self,):
        self.get_current_url()
        self.click_checkout()