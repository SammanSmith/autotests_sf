from api2 import PetFriends2
from settings import valid_email, valid_password


pf = PetFriends2()

auth_key = ''


def test_get_api_key_for_valid_user(get_api_key):
    status, result = get_api_key
    global auth_key
    assert status == 200
    assert 'key' in result
    if 'key' in result:
        auth_key = result['key']

def test_get_all_pets_with_valid_key(filter=''):
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_pet_with_valid_key():
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, 'Babai', 'Cat', '33', 'img/cat.jpg')
    assert status == 200
    assert result['name'] == 'Babai'
    assert result['id'] != ''

def test_delete_pet_with_valid_key(filter=''):
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    if len(result['pets']) > 0:
        status = pf.delete_pet(auth_key, result['pets'][0]['id'])
    else:
        _, result = pf.add_new_pet(auth_key, 'Babai', 'Cat', '33', 'img/cat.jpg')
        status = pf.delete_pet(auth_key, result['id'])
    assert status == 200

def test_update_info_about_pet_valid():
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, 'Babai', 'Cat', '33', 'img/cat.jpg')
    status, result = pf.update_pet(auth_key, result['id'], 'BlackFury', 'Dragon', 1000)
    assert status == 200

def test_add_new_pet_without_photo_valid():
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, 'Bobik', 'Dog', 5)
    assert status == 200
    assert result['name'] == 'Bobik'

def test_set_my_pet_photo_valid():
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter='my_pets')

    if len(result['pets']) > 0:
        status, result = pf.set_photo_pet(auth_key, result['pets'][0]['id'], 'img/redgato.jpg')
    else:
        _, result = pf.add_new_pet(auth_key, 'Jack', 'Sparrow', 10, 'img/cat.jpg')
        status, result = pf.set_photo_pet(auth_key, result['pets'][0]['id'], 'img/redgato.jpg')
    assert status == 200
    # assert result['id']

def test_set_other_pet_photo_invalid():
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter='')

    if len(result['pets']) > 0:
        status, result = pf.set_photo_pet(auth_key, result['pets'][0]['id'], 'img/redgato.jpg')
    else:
        _, result = pf.add_new_pet(auth_key, 'Jack', 'Sparrow', 10, 'img/cat.jpg')
        status, result = pf.set_photo_pet(auth_key, result['pets'][0]['id'], 'img/redgat.jpg')
    assert status == 400 or status == 500

def test_set_other_pet_photo_invalid_auth_key():
    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter='')

    if len(result['pets']) > 0:
        status, result = pf.set_photo_pet(auth_key+'xx', result['pets'][0]['id'], 'img/redgato.jpg')
    else:
        _, result = pf.add_new_pet(auth_key, 'Jack', 'Sparrow', 10, 'img/cat.jpg')
        status, result = pf.set_photo_pet(auth_key, result['pets'][0]['id'], 'img/redgato.jpg')
    assert status == 403

def test_get_api_key_for_invalid_user():
    status, result = pf.get_api_key('matreshka@mail.ru', 'dasdwrasfa')
    assert status == 403
