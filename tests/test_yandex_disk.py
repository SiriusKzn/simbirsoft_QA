import uuid

import pytest
from data import generators as gen

from handlers import url_disk_handler as handlers


class Test_Disk_API:
    test_params = [
        {
            'Folder_name': f"__{gen.generate_folder_name()}__",
            'File_name': str(uuid.uuid4())[24:]
        },
        # {
        #     'Folder_name': "0test_name@",
        #     'File_name': str(uuid.uuid4())[24:]
        # },
        # {
        #     'Folder_name': ".testName.",
        #     'File_name': str(uuid.uuid4())[24:]
        # }
    ]

    @pytest.fixture(scope='class', autouse=True, params=test_params)
    def prepare(self, request):
        self = request.cls
        self.test_params = request.param

    def test_create_folder(self):
        response = handlers.create_folder(self.test_params["Folder_name"])
        json = response.json()
        assert 'message' not in json, f"{json.get('message')}"
        assert response.status_code == 201, "Папка не была создана"

    def test_move_folder(self):
        response = handlers.copy_file("Файл для копирования.docx",
                                      f"/{self.test_params['Folder_name']}/Файл для копирования.docx")
        json = response.json()
        assert 'message' not in json, f"{json.get('message')}"
        assert response.status_code == 201, "Папка не была перемещена"

    def test_rename_file(self):
        response = handlers.rename_file(f"/{self.test_params['Folder_name']}/Файл для копирования.docx",
                                        f"/{self.test_params['Folder_name']}/{self.test_params['File_name']}.docx")
        json = response.json()
        assert 'message' not in json, f"{json.get('message')}"
        assert response.status_code == 201, "Файл не был переименован"

    # @pytest.mark.skip("Не используется в данном тест-кейсе")
    # def test_delete_folder(self):
    #     response = handlers.delete_file(f"/{self.test_params['Folder_name']}")
    #     json = response.json()
    #     assert 'message' not in json, f"{json.get('message')}"
    #     assert response.status_code == 202, "Файл не был переименован"
