from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from page_store.locators import StoreLocators
from data.user_data import UserData


class StorePage:

    def __init__(self):
        self.locators = StoreLocators()
        self.driver = webdriver.Chrome()
        self.data = UserData()

    def open_browser(self):
        browser = self.driver
        browser.get('https://www.saucedemo.com/')

    def authorization(self):
        input_user_name = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.USER_NAME))
        input_user_name.send_keys(self.data.username)
        input_password = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.PASSWORD))
        input_password.send_keys(self.data.password)
        button_login = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.BUTTON_LOGIN))
        button_login.click()

    def add_product(self):
        product = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.PRODUCT))
        product.click()

    def go_to_shopping_cart(self):
        shopping_cart = Wait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.locators.SHOPPING_CART))
        shopping_cart.click()

    def check_product(self):
        product = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.CHECK_PRODUCT))
        return product.text

    def click_checkout(self):
        checkout = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.CHECKOUT_BUTTON))
        checkout.click()

    def fill_information(self):
        first_name = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.FIRST_NAME))
        last_name = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.LAST_NAME))
        postal_code = Wait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.locators.POSTAL_CODE))
        first_name.send_keys(self.data.first_name)
        last_name.send_keys(self.data.last_name)
        postal_code.send_keys(self.data.postal_code)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 150);")

    def click_continue_button(self):
        continue_button = Wait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.locators.BUTTON_CONTINUE))
        continue_button.click()

    def click_finish_button(self):
        finish_button = Wait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.locators.FINISH_BUTTON))
        finish_button.click()

    def check_finally_inscription(self):
        finally_inscription = Wait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.locators.FINALLY_INSCRIPTION))
        return finally_inscription.text
