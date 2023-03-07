import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru'

    def get_api_key(self, email: str, password: str):
        """
        Этот метод позволяет получить ключ API,
        который следует использовать для других методов API.

        :param email: str
        :param password: str
        :return: status code & json or text
        """
        headers = {
            'email': email,
            'password': password
        }

        response = requests.get(self.base_url+'/api/key', headers=headers)
        status = response.status_code
        try:
            result = response.json()
        except BaseException:
            result = response.text

        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """
        Этот метод позволяет получить список питомцев

        :param auth_key:
        :param filter:
        :return: status code & json or text
        """
        headers = {
            'auth_key': auth_key['key']
        }

        filter = {
            'filter': filter
        }

        response = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)
        status = response.status_code
        try:
            result = response.json()
        except BaseException:
            result = response.text

        return status, result

    def add_new_pets(self, auth_key, name, animal_type, age, pet_photo):
        """
        Этот метод позволяет добавить информацию о новом питомце.

        :param auth_key:
        :param name:
        :param animal_type:
        :param age:
        :param pet_photo:
        :return: status code & json or text
        """
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            }
        )

        headers = {
            'auth_key': auth_key['key'],
            'Content-Type': data.content_type
        }

        response = requests.post(self.base_url+'/api/pets', data=data, headers=headers)
        status = response.status_code
        try:
            result = response.json()
        except BaseException:
            result = response.text

        return status, result

    def delete_pet(self, auth_key, pet_id):
        """
        Этот метод позволяет удалить информацию о питомце из базы данных.

        :param auth_key:
        :param pet_id:
        :return:
        """

        headers = {'auth_key': auth_key['key']}

        response = requests.delete(f'{self.base_url}/api/pets/{pet_id}', headers=headers)
        status = response.status_code

        return status

    def update_pet(self, auth_key, pet_id, name, animal_type, age):
        """
        Этот метод позволяет обновить информацию о питомце.

        :param auth_key:
        :param pet_id:
        :param name:
        :param animal_type:
        :param age:
        :return:
        """
        headers = {
            'auth_key': auth_key['key']
        }

        formData = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        response = requests.put(f'{self.base_url}/api/pets/{pet_id}', headers=headers, data=formData)
        status = response.status_code
        try:
            result = response.json()
        except BaseException:
            result = response.text

        return status, result
