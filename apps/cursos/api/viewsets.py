from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.cursos.api.serializers import CursoSerializer, AvaliacaoSerializer
from apps.cursos.models import Curso, Avaliacao


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

