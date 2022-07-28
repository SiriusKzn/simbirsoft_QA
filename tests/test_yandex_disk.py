
import pytest
from data import data
from pages.auth_page import AuthPage
from pages.disk_page import DiskPage


class TestDisk:
    """Генерация параметров для теста"""
    test_params = [
        {
            'Folder_name': f"__{data.generate_folder_name()}__",
            # },
            # {
            #     'Folder_name': f"0_{data.generate_folder_name()}_0",
            # },
            # {
            #     'Folder_name': f".{data.generate_folder_name()}.",
        }
    ]

    @pytest.fixture(scope='class', autouse=True, params=test_params)
    def prepare(self, request):
        self = request.cls
        self.test_params = request.param
        data.generate_folder_name()

    @pytest.mark.main
    def test_copy_file(self, driver):
        AuthPage(driver, "https://yandex.ru/").login()
        disk_page = DiskPage(driver, "https://disk.yandex.ru/client/disk")
        disk_page.open()
        disk_page.create_folder(self.test_params["Folder_name"])
        disk_page.copy_file(data.NAME_FILE, self.test_params["Folder_name"])
        disk_page.go_to_file(self.test_params["Folder_name"])
        result_list = disk_page.get_files_name_list()

        assert data.NAME_FILE in result_list, "Файл не найден, либо изменилось имя."

    @pytest.mark.optional
    def test_upload_file_and_check_text(self, driver):
        folder_name = self.test_params["Folder_name"] + "[Optional test]"
        AuthPage(driver, "https://yandex.ru/").login()
        disk_page = DiskPage(driver, "https://disk.yandex.ru/client/disk")
        disk_page.open()
        disk_page.create_folder(folder_name)
        driver.refresh()
        disk_page.go_to_file(name_folder=folder_name)
        file_name = disk_page.upload_file(wait=2)
        disk_page.go_to_file(name_folder=file_name)
        disk_page.change_tab(driver=driver, id=1)

        assert disk_page.get_list_from_text(driver) == data.prepare_file_to_compare(), 'Содержание файла не ' \
                                                                                       'соответствует исходному. '
        assert driver.title == file_name, "Название не соответствует исходному"

    """Удаление созданных папок после прохождения теста """
    # @pytest.mark.skip("Не используется в тест-кейсе")
    # def test_clean_test_disk(self, driver):
    #     AuthPage(driver, "https://yandex.ru/").login()
    #     disk_page = DiskPage(driver, "https://disk.yandex.ru/client/disk")
    #     disk_page.open()
    #     disk_page.delete_folder(self.test_params["Folder_name"])
    #     disk_page.clean_trash()
