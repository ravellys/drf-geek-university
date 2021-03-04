from random import randint

import requests


headers = {'Authorization': 'Token 23e3470b4989a5eaeb85183fe807bfd2ebb9016c'}
url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

curso_update = {
    "titulo": "update curso",
    "url": f"http://www.teste{randint(1, 100000)}.com"
}

result = requests.put(url=f'{url_cursos}2/', headers=headers, data=curso_update)

# teste status HTTP 200
assert result.status_code == 200
assert result.json()['titulo'] == curso_update['titulo']