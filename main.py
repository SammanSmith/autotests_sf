import requests

status = 'available'

resp = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                    headers={'accept': 'application/json'})

print(resp.status_code)
print(resp.text)
print(resp.json())
print(type(resp.json()))