import requests


# GET avaliacoes
url_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'
avaliacoes = requests.get(url_avaliacoes)

assert avaliacoes.status_code == 200
assert avaliacoes.json()['count'] == 8


# GET cursos
headers = {'Authorization': 'Token 23e3470b4989a5eaeb85183fe807bfd2ebb9016c'}
url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
cursos = requests.get(url=url_cursos, headers=headers)
