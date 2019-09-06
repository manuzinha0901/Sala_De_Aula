from rest_framework import serializers
from .models import Professor


class ProfessorSeralizer(serializers.ModelSerializer):
     class Meta:
         model = Professor 
         fields =('nome','idade',)