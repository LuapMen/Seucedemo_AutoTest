import time
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_linnc_abaut():
    os.environ['PATH'] += ';E:\\Project\\Project_Seucedemo_Selenium\\Driver'
    driver = webdriver.Chrome()

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_menu_about()



    time.sleep(5)

