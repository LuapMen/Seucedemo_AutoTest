
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    select_product_1 = "//*[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//*[@id='shopping_cart_container']/a"
    menu = "//*[@id='react-burger-menu-btn']"
    link_about = "//*[@id='about_sidebar_link']"


    #Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.menu)))

    def get_about(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable ((By.XPATH,self.link_about)))
    #actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("click add to cart product 1")

    def click_cart(self):
        self.get_cart().click()
        print("click cart")

    def click_menu(self):
        self.get_menu().click()
        print("click menu")

    def click_about(self):
        self.get_about().click()
        print("click about")


    #Methods
    def select_product(self,):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_menu_about(self,):
        self.get_current_url()
        self.click_menu()
        self.click_about()
        self.assert_url('https://saucelabs.com/')