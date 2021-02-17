from rest_framework import generics
from rest_framework.generics import get_object_or_404

from apps.cursos.api.serializers import AvaliacaoSerializer, CursoSerializer
from apps.cursos.models import Avaliacao, Curso


# List e Create
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


# Detail, Delete e Update
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(queryset=self.queryset,
                                     curso_id=self.kwargs.get('curso_pk'),
                                     id=self.kwargs.get('avaliacao_pk'))
        return super().get_object()
