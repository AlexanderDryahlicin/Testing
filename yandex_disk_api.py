import requests
import os


class YandexDiskAPI:
    def __init__(self, token: str):
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {
            "Authorization": f"OAuth {token}",
            "Content-Type": "application/json"
        }

    def create_folder(self, folder_name: str) -> int:
        url = f"{self.base_url}/resources"
        params = {
            "path": folder_name,
            "overwrite": "false"
        }
        response = requests.put(url, headers=self.headers, params=params)
        return response.status_code

    def check_folder_exists(self, folder_name: str) -> bool:
        url = f"{self.base_url}/resources"
        params = {
            "path": folder_name
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.status_code == 200


if __name__ == "__main__":
    ya_token = os.getenv("YANDEX_DISK_TOKEN", "TOKEN")
    ya_api = YandexDiskAPI(ya_token)

    folder_name = "test_folder"
    status = ya_api.create_folder(folder_name)
    print(f"Статус создания папки: {status}")

    exists = ya_api.check_folder_exists(folder_name)
    print(f"Папка существует: {exists}")