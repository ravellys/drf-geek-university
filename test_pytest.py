from random import randint

import requests


class TestCursos:
    headers = {'Authorization': 'Token 23e3470b4989a5eaeb85183fe807bfd2ebb9016c'}
    url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
    novo = {
        "titulo": "novo",
        "url": f"http://www.teste{randint(1, 100000)}.com"
    }
    update = {
        "titulo": "update",
        "url": f"http://www.teste{randint(1, 100000)}.com"
    }

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_cursos, headers=self.headers)
        assert cursos.status_code == 200

    def test_post_curso(self):
        result = requests.post(url=self.url_cursos, headers=self.headers, data=self.novo)
        assert result.status_code == 201
        assert result.json()['titulo'] == self.novo['titulo']
        requests.delete(url=f'{self.url_cursos}{result.json()["id"]}/', headers=self.headers)

    def test_put_curso(self):
        id = self.post_teste()
        result = requests.put(url=f'{self.url_cursos}{id}/', headers=self.headers, data=self.update)
        # teste status HTTP 200
        assert result.status_code == 200
        assert result.json()['titulo'] == self.update['titulo']
        requests.delete(url=f'{self.url_cursos}{id}/', headers=self.headers)

    def test_delete_curso(self):
        id = self.post_teste()
        result = requests.delete(url=f'{self.url_cursos}{id}/', headers=self.headers)
        # teste status HTTP 200
        assert result.status_code == 204
        assert len(result.text) == 0
        result = requests.delete(url=f'{self.url_cursos}{id}/', headers=self.headers)
        assert result.status_code == 404

    def post_teste(self):
        novo = {
            "titulo": "novo",
            "url": f"http://www.teste{randint(1, 100000)}.com"
        }
        return requests.post(url=self.url_cursos, headers=self.headers, data=novo).json()['id']



