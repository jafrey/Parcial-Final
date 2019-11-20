from django.shortcuts import render

# Create your views here.

#libreria para que django nos deje enviar huevadas
from django.shortcuts import render, render_to_response

#librerias de rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView


#librerias de rest_framework relacionadas con la autenticacion
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

#libreria para que el csrf no rompa los huevos
from django.views.decorators.csrf import csrf_exempt


#importamos los serializadores
from .serializers import UserSerializer, CancionSerializer

#importamos los modelos usados y que vamos a usar para crear los viewsets
from .models import Cancion
from django.contrib.auth.models import User

#librerias requests que sirven para consumir las apis
import requests

#libreria json, medio al pedo pero por las dudas
import json

########################################### Comienzan las views


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset de los usuarios
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CancionViewSet(viewsets.ModelViewSet):
    """
    Viewset de los Canciones
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CancionSerializer
    queryset = Cancion.objects.all()
