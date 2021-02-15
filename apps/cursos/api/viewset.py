from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cursos.api.serializers import AvaliacaoSerializer, CursoSerializer
from apps.cursos.models import Avaliacao, Curso


class CursoAPIView(APIView):
    """
    API de cursos
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API de avaliacao
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
