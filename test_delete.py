from random import randint

import requests


headers = {'Authorization': 'Token 23e3470b4989a5eaeb85183fe807bfd2ebb9016c'}
url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

novo = {
    "titulo": "update curso",
    "url": f"http://www.teste{randint(1, 100000)}.com"
}
result = requests.post(url=url_cursos, headers=headers, data=novo)

id = result.json()['id']
result = requests.delete(url=f'{url_cursos}{id}/', headers=headers)

# teste status HTTP 200
assert result.status_code == 204
assert len(result.text) == 0

result = requests.delete(url=f'{url_cursos}{id}/', headers=headers)
assert result.status_code == 404