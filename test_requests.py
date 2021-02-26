import requests

# GET para avaliações
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')
print("status:", avaliacoes.status_code)
print("dados resposta:", avaliacoes.json())
print("tipo dos dados:", type(avaliacoes.json()))

# Acesso da quantidade de registros
print('quantidade registros:', avaliacoes.json()['count'])
avaliacoes_next = requests.get(avaliacoes.json()['next'])
print('avaliações da próxima pagna:', avaliacoes_next.json())


# GET cursos

headers = {'Authorization': 'Token 23e3470b4989a5eaeb85183fe807bfd2ebb9016c'}
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)
print("dados cursos:", cursos.json())
