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


def test_buy_product():
    os.environ['PATH'] += ';E:\\Project\\Project_Seucedemo_Selenium\\Driver'
    driver = webdriver.Chrome()

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_product()

    cart_page = Cart_page(driver)
    cart_page.click_checkout()

    chp = Checkout_page(driver)
    chp.checkout_continue()

    pg = Payment_page(driver)
    pg.click_finish()

    fp = Finish_page(driver)
    fp.finish()

    time.sleep(5)

