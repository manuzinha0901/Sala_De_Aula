from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Aluno
from .serialozers import AlunoSeralizer

class AlunoViewSet(viewsets.ModelViewSet):
    filter_backends = [searchFilter]
    search_Filter = ['^nome','=idade']
    queryset = Aluno.objects.all()
    permissions_class = (IsAuthenticatedOrReadOnly,)
    authentication_class = (TokenAuthentication,)
    serializer_class = AlunoSeralizer

class AlunoSeralizer(AlunoSeralizers.ModelViewSet):
    class


# Create your views here.
