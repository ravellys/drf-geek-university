from rest_framework import serializers
from apps.cursos.models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}  # não mostra emails na consulta
        }
        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação percisa ser um inteiro de 1 a 5')


class CursoSerializer(serializers.ModelSerializer):
    # Nested relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes')


# Testando serializers
# >>> from rest_framework.renderers import JSONRenderer
# >>> from apps.cursos.models import Avaliacao, Curso
# >>> from apps.cursos.api.serializers import CursoSerializer

# >>> curso = Curso.objects.latest('id')
# >>> serializer = CursoSerializer(curso)
# >>> serializer.data
# >>> JSONRenderer().render(serializer.data)
