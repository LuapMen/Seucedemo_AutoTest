


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  base.base_class import Base

class Checkout_page(Base):

    #User
    # first_name_1 = "user"
    # last_name_1 = "last name"
    # postal_code = "31-636"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    first_name = "//*[@id='first-name']"
    last_name = "//*[@id='last-name']"
    zip_postal_code = "//*[@id='postal-code']"
    continue_button = "//*[@id='continue']"


    #Getters
    def get_first_name(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.last_name)))

    def get_zip_postal_code(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.zip_postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.continue_button)))

    #actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last name")

    def input_zip_postal_code(self, zip_postal_code):
        self.get_zip_postal_code().send_keys(zip_postal_code)
        print("input zip / postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("click checkout")


    #Methods

    def checkout_continue(self,):
        self.get_current_url()
        self.input_first_name("user")
        self.input_last_name("last name")
        self.input_zip_postal_code("31-636")
        self.click_continue_button()