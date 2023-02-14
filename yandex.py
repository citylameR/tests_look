from pprint import pprint
from config.py import TOKEN
import yadisk
import requests



class YANDEX:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
        
            'contentType': 'application/json',
            'Authorization': f'OAuth {self.token}'

        }

    def get_all_file(self):
        uri = 'v1/disk/resources/files/'
        request_url = self.base_host + uri
        response = requests.get(request_url, headers=self.get_headers())
        pprint(response.json())

    def get_status_code(self):
        uri = 'v1/disk/resources/files/'
        request_url = self.base_host + uri
        response = requests.get(request_url, headers=self.get_headers())
        pprint(response.status_code)

    def check_folder_creation(self):
        uri = 'v1/disk/resources'
        request_url = self.base_host + uri
        response = requests.put(f'{request_url}?path=TESTNETOLOGIA', headers=self.get_headers())
        print(response.status_code)

        return response.status_code

    def check_folder_deleted(self):
        uri = 'v1/disk/resources'
        request_url = self.base_host + uri
        response = requests.delete(f'{request_url}?path=TESTNETOLOGIA', headers=self.get_headers())
        return response.status_code


# if __name__ == '__main__':
#     ya = YANDEX(TOKEN)
#     ya.get_all_file()
#     print('---' * 100)
#     ya.get_status_code()
#     print('---' * 100)
#     # ya.check_folder_creation()
#     print('---' * 100)
#     ya.check_folder_deleted()
