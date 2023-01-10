from .base_page import BasePage
from .locators import AuthLocators


class RegistrPage(BasePage):

    def __init__(self, driver, timeout=10, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/'
        driver.get(url)
        driver.find_element(*AuthLocators.register_link).click()

        self.first_name = driver.find_element(*AuthLocators.first_name)
        self.last_name = driver.find_element(*AuthLocators.last_name)
        self.address_registration = driver.find_element(*AuthLocators.address_registration)
        self.email_registration = driver.find_element(*AuthLocators.email_registration)
        self.passw_registration = driver.find_element(*AuthLocators.passw_registration)
        self.passw_registration_confirm = driver.find_element(*AuthLocators.passw_registration_confirm)
        self.registration_btn = driver.find_element(*AuthLocators.registration_btn)
        self.page_left_registration = driver.find_element(*AuthLocators.page_left_registration)
        self.card_of_registration = driver.find_element(*AuthLocators.card_of_registration)
        self.container_f_name = driver.find_element(*AuthLocators.container_f_name)
        self.container_l_name = driver.find_element(*AuthLocators.container_l_name)
        self.container_passw_confirm = driver.find_element(*AuthLocators.container_passw_confirm)

    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)
