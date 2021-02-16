from rest_framework import status
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

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # verificar se é válido, caso não seja retorna uma excessão e finaliza
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de avaliacao
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
