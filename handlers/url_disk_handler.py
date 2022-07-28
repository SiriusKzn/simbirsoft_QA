import requests

from data import config

host = "https://cloud-api.yandex.net"
headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': f'OAuth {config.API_TOKEN}'
           }


def create_folder(folder_name):
    response = requests.request(method="PUT",
                                url=f"{host}/v1/disk/resources" + f"?path={folder_name}",
                                headers=headers)
    return response


def copy_file(from_path, to_path):
    response = requests.request(method="POST",
                                url=f"{host}/v1/disk/resources/copy" + f"?from={from_path}&path={to_path}",
                                headers=headers)
    return response

def rename_file(from_name, to_name):
    response = requests.request(method="POST",
                                url=f"{host}/v1/disk/resources/move" + f"?from={from_name}&path={to_name}",
                                headers=headers)
    return response

def delete_file(path):
    response = requests.request(method="DELETE",
                                url=f"{host}/v1/disk/resources/" + f"?path={path}",
                                headers=headers)
    return response

