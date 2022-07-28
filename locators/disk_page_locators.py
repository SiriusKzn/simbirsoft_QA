from selenium.webdriver.common.by import By

"""Локаторы для взаимодействия с страницей Я.Диск"""
class DiskPageLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, "span[class='create-resource-popup-with-anchor']")
    CREATE_FOLDER_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Папку']")
    NAME_FOLDER_TEXTBOX = (By.XPATH, "//form/span/input")
    SAVE_NAME_BUTTON = (By.CSS_SELECTOR, "button[class='Button2 Button2_view_action Button2_size_m "
                                         "confirmation-dialog__button confirmation-dialog__button_submit ']")
    ERROR_SAVE_FOLDER_TEXT = (By.CSS_SELECTOR, "div[class='rename-dialog__rename-error']")
    NAME_FILES_TEXT = (By.CSS_SELECTOR, "div[class='listing-item__title listing-item__title_overflow_clamp']")
    COPY_BTN = (By.CSS_SELECTOR, "div[value='copy']")
    COPY_BTN_DIALOG_BTN = (By.CSS_SELECTOR, "button[class='Button2 Button2_view_action Button2_size_m "
                                            "confirmation-dialog__button confirmation-dialog__button_submit ']")
    NAME_CATALOG = (By.CSS_SELECTOR, "div[class='listing-heading__title-inner']")
    DELETE_BTN = (By.CSS_SELECTOR, "div[value='delete']")
    CLEAN_TRASH_BTN = (By.CSS_SELECTOR, "div[value='clean-trash']")
    SUBMIT_CLEAN_TRASH_BTN = (By.CSS_SELECTOR, "button[class='Button2 Button2_view_action Button2_size_m "
                                               "confirmation-dialog__button confirmation-dialog__button_submit ']")
    UPLOAD_BTN = (By.CSS_SELECTOR, "input[class='upload-button__attach']")
    PARAGRAPH_TEXT = (By.CLASS_NAME, "mg1")
    INPUT_PAGE_BOX = (By.CSS_SELECTOR, "input[type='number']")

