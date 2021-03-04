from random import randint

import requests


headers = {'Authorization': 'Token 23e3470b4989a5eaeb85183fe807bfd2ebb9016c'}
url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

novo = {
    "titulo": "teste",
    "url": f"http://www.teste{randint(1, 100000)}.com"
}

result = requests.post(url=url_cursos, headers=headers, data=novo)

# teste status HTTP 201
assert result.status_code == 201
assert result.json()['titulo'] == novo['titulo']