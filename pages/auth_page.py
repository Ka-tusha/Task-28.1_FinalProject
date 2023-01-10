from .base_page import BasePage
from .locators import AuthLocators


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)

        self.tub_phone = driver.find_element(*AuthLocators.tub_phone)
        self.active_tub_phone = driver.find_element(*AuthLocators.active_tub_phone)
        self.tub_email = driver.find_element(*AuthLocators.tub_email)
        self.email = driver.find_element(*AuthLocators.auth_email)
        self.pass_eml = driver.find_element(*AuthLocators.auth_pass_eml)
        self.btn_enter = driver.find_element(*AuthLocators.auth_btn_enter)
        self.tub_login = driver.find_element(*AuthLocators.tub_login)
        self.login = driver.find_element(*AuthLocators.auth_login)
        self.pass_log = driver.find_element(*AuthLocators.auth_pass_log)
        self.tub_ls = driver.find_element(*AuthLocators.tub_ls)
        self.placeholder_name_of_user = driver.find_element(*AuthLocators.placeholder_name_of_user)
        self.forgot_password_link = driver.find_element(*AuthLocators.forgot_password_link)
        self.register_link = driver.find_element(*AuthLocators.register_link)
        self.page_right = driver.find_element(*AuthLocators.page_right)
        self.page_left = driver.find_element(*AuthLocators.page_left)
        self.card_of_auth = driver.find_element(*AuthLocators.card_of_auth)
        self.menu_tub = driver.find_element(*AuthLocators.menu_tub)

    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)
