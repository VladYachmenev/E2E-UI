from selenium.webdriver.common.by import By


class StoreLocators:
    USER_NAME = (By.CSS_SELECTOR, 'input#user-name')
    PASSWORD = (By.CSS_SELECTOR, 'input#password')
    BUTTON_LOGIN = (By.CSS_SELECTOR, 'input#login-button')

    PRODUCT = (By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack')
    SHOPPING_CART = (By.CSS_SELECTOR, 'a.shopping_cart_link')
    CHECK_PRODUCT = (By.CSS_SELECTOR, 'div.inventory_item_name')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'button#checkout')

    FIRST_NAME = (By.CSS_SELECTOR, 'input#first-name')
    LAST_NAME = (By.CSS_SELECTOR, 'input#last-name')
    POSTAL_CODE = (By.CSS_SELECTOR, 'input#postal-code')
    BUTTON_CONTINUE = (By.CSS_SELECTOR, 'input#continue')
    FINISH_BUTTON = (By.CSS_SELECTOR, 'button#finish')
    FINALLY_INSCRIPTION = (By.CSS_SELECTOR, 'h2.complete-header')
