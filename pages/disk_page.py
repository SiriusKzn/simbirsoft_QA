import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from data import data
from locators.disk_page_locators import DiskPageLocators
from pages.base_page import BasePage


class DiskPage(BasePage):
    locators = DiskPageLocators()

    """Создание папки"""
    def create_folder(self, name_folder):
        self.element_is_visible(self.locators.CREATE_BUTTON).click()
        self.element_is_visible(self.locators.CREATE_FOLDER_BUTTON).click()
        input_box = self.element_is_visible(self.locators.NAME_FOLDER_TEXTBOX)
        self.clear_inputbox(input_box)
        input_box.send_keys(name_folder)
        self.element_is_visible(self.locators.SAVE_NAME_BUTTON).click()
        if self.element_is_visible(self.locators.ERROR_SAVE_FOLDER_TEXT).text:
            pytest.skip("Skip this test. The folder already exists.")

    """Копирование файла"""
    def copy_file(self, name, name_folder):
        list_files = self.get_files_list()
        for element in list_files:
            if element.get_attribute("aria-label").split('.')[0] == name:
                time.sleep(1)
                self.action_right_click(element)
        self.element_is_visible(self.locators.COPY_BTN).click()
        self.element_is_visible((By.CSS_SELECTOR, f"div[title='{name_folder}']")).click()
        self.element_is_visible(self.locators.COPY_BTN_DIALOG_BTN).click()

    """Двойной клик по файлу"""
    def go_to_file(self, name_folder):
        list_files = self.get_files_list()
        for element in list_files:
            if element.get_attribute("aria-label") == name_folder:
                self.action_double_click(element)
                break

    """Удаление файла в Я.Диске"""
    def delete_file(self, name_file):
        list_files = self.get_files_list()
        for element in list_files:
            if element.get_attribute("aria-label") == name_file:
                self.action_right_click(element)
                self.element_is_visible(self.locators.DELETE_BTN).click()
                break

    """Очищение корзины в Я.Диске"""
    def clean_trash(self):
        list_files = self.get_files_list()
        for element in list_files:
            if element.get_attribute("aria-label") == "Корзина":
                self.action_right_click(element)
                self.element_is_visible(self.locators.CLEAN_TRASH_BTN).click()
                self.element_is_visible(self.locators.SUBMIT_CLEAN_TRASH_BTN).click()
                break

    """Загрузка файла на сервер Я.Диск"""
    def upload_file(self, wait):
        self.element_is_present(self.locators.UPLOAD_BTN).send_keys(data.FILE_PATH)
        time.sleep(wait)
        return data.FILE_PATH.split('\\')[-1]

    """Чтение файла на сервере"""
    def get_list_from_text(self, driver):
        elements_list = []
        count = self.get_count_pages(driver)
        for i in range(1, count):
            self.go_to_page(i)
            elements_list = self.get_list(elements_list)
        return elements_list

    """Сохранение в list текста элементов, находящихся в зоне видимости"""
    def get_list(self, res_list):
        elements_list = self.elements_are_presents(locator=(By.CLASS_NAME, "mg1"))
        for list in elements_list:
            if list.text not in res_list:
                res_list.append(list.text)
        return res_list

    """Переход на страницу"""
    def go_to_page(self, page):
        element = self.element_is_present(self.locators.INPUT_PAGE_BOX)
        self.clear_inputbox(element)
        element.send_keys(page)
        element.send_keys(Keys.ENTER)

    """Получение количества страниц в документе"""
    def get_count_pages(self, driver):
        count = 1
        element = self.element_is_present(self.locators.INPUT_PAGE_BOX)
        if element:
            while True:
                count += 1
                element.click()
                self.clear_inputbox(element)
                element.send_keys(count)
                element.send_keys(Keys.ENTER)
                element = self.element_is_present(self.locators.INPUT_PAGE_BOX)
                if element.get_attribute('value') == str(count-1):
                    break
        return count

    """Получение имен файлов в папке"""
    def get_files_name_list(self):
        list_elements = self.elements_are_visible(self.locators.NAME_FILES_TEXT)
        result_list = []
        for file in list_elements:
            result_list.append(file.get_attribute("aria-label").split('.')[0])
        return result_list

    """Получение элементов файлов в папке"""
    def get_files_list(self):
        return self.elements_are_visible(self.locators.NAME_FILES_TEXT)



