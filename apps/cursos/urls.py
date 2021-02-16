from django.urls import path

from apps.cursos.api.viewset_genericsview import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),

    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]