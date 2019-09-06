from rest_framework import serializers
from .models import Aluno


class AlunoSeralizer(serializers.ModelSerializer):
     class Meta:
         model = Aluno 
         fields =('nome','idade','email')








