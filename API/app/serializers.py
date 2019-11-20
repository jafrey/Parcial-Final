#importa el user desde las tablas de django
from django.contrib.auth.models import User

#importamos el/los modelo/s
from .models import Cancion

#importamos los serializadores
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

class CancionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cancion
        fields = ['id', 'nom_cancion', 'desc_cancion']
