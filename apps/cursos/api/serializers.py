from rest_framework import serializers
from apps.cursos.models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}  # não mostra emails na consulta
        }
        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo')


# Testando serializers
# >>> from rest_framework.renderers import JSONRenderer
# >>> from apps.cursos.models import Avaliacao, Curso
# >>> from apps.cursos.api.serializers import CursoSerializer

# >>> curso = Curso.objects.latest('id')
# >>> serializer = CursoSerializer(curso)
# >>> serializer.data
# >>> JSONRenderer().render(serializer.data)
