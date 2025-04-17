import unittest
from unittest.mock import patch, MagicMock
import os
from yandex_disk_api import YandexDiskAPI

class TestYandexDiskAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token = os.getenv("YANDEX_DISK_TOKEN", "y0__xCfs7HhBxj7izcgjo3E7RI75yt9aIEnxN1rxmWRemJ6p42vcA&token_type=bearer&expires_in=31536000&cid=qjcnpceyj2f5qumeg98raheqfw")
        cls.api = YandexDiskAPI(cls.token)
        cls.test_folder = "test_folder"

    @patch('requests.put')
    def test_create_folder_success(self, mock_put):
        """Тест успешного создания папки"""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_put.return_value = mock_response

        status = self.api.create_folder(self.test_folder)
        self.assertEqual(status, 201)

    @patch('requests.put')
    def test_create_folder_conflict(self, mock_put):
        """Тест попытки создания уже существующей папки"""
        mock_response = MagicMock()
        mock_response.status_code = 409
        mock_put.return_value = mock_response

        status = self.api.create_folder(self.test_folder)
        self.assertEqual(status, 409)

    @patch('requests.put')
    def test_create_folder_unauthorized(self, mock_put):
        """Тест с неверным токеном"""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_put.return_value = mock_response

        status = self.api.create_folder(self.test_folder)
        self.assertEqual(status, 401)

    @patch('requests.get')
    def test_check_folder_exists_true(self, mock_get):
        """Тест проверки существующей папки"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        exists = self.api.check_folder_exists(self.test_folder)
        self.assertTrue(exists)

    @patch('requests.get')
    def test_check_folder_exists_false(self, mock_get):
        """Тест проверки несуществующей папки"""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        exists = self.api.check_folder_exists(self.test_folder)
        self.assertFalse(exists)

    @patch('requests.put')
    def test_create_folder_bad_request(self, mock_put):
        """Тест с некорректными параметрами запроса"""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_put.return_value = mock_response

        status = self.api.create_folder("")
        self.assertEqual(status, 400)


if __name__ == "__main__":
    unittest.main()