import requests
import jsonpath

# GET para avaliações
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
print(resultados, '\n')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(resultados, '\n')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(resultados, '\n')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[:].nome')
print(resultados, '\n')