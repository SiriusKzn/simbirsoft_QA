from selenium.webdriver.common.by import By

"""Локаторы для взаимодествия с страницой Входа"""


class AuthPageLocators:
    MAIL_BUTTON = (By.CSS_SELECTOR, "button[data-type='login']")
    HOME_LOGIN_BUTTON = (By.CSS_SELECTOR, "a[class='home-link desk-notif-card__login-new-item "
                                          "desk-notif-card__login-new-item_enter home-link_black_yes "
                                          "home-link_hover_inherit']")
    HOME_LOGO = (By.CSS_SELECTOR, "div[class='home-logo__default']")
    LOGIN_TEXTBOX = (By.CSS_SELECTOR, "input[id='passp-field-login']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, "input[id='passp-field-passwd']")
