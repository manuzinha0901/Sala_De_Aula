from django.shortcuts import render
from rest_framework import viewsets

from professor.models import Professor
from professor.serialozers import ProfessorSeralizer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSeralizer
    