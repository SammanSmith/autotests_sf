from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_pet_with_valid_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, 'Babai', 'Cat', '33', 'img/cat.jpg')
    assert status == 200
    assert result['name'] == 'Babai'
    assert result['id'] != ''

def test_delete_pet_with_valid_key(filter=''):
    # сделать проверку, что список своих питомцев не пуст
    # если пуст создать и далее по списку
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    if len(result['pets']) > 0:
        status = pf.delete_pet(auth_key, result['pets'][0]['id'])
    else:
        _, result = pf.add_new_pets(auth_key, 'Babai', 'Cat', '33', 'img/cat.jpg')
        status = pf.delete_pet(auth_key, result['id'])
    assert status == 200

def test_update_info_about_pet_valid():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pets(auth_key, 'Babai', 'Cat', '33', 'img/cat.jpg')
    status, result = pf.update_pet(auth_key, result['id'], 'BlackFury', 'Dragon', 1000)
    assert status == 200
