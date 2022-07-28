import time

import pytest
import webdriver_manager.drivers.chrome

from data import data
from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):

    locators = AuthPageLocators()

    def login(self):
        self.open()
        self.element_is_clickable(self.locators.HOME_LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.MAIL_BUTTON).click()
        self.element_is_visible(self.locators.LOGIN_TEXTBOX).send_keys(data.YA_LOGIN)
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.PASSWORD_TEXTBOX).send_keys(data.YA_PASS)
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.HOME_LOGO)
