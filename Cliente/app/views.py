from django.shortcuts import render, render_to_response

#libreria para que el csrf no rompa los huevos
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#libreria requests, que nos sirve para consumir apis
import requests

#libreria json, medio al pedo pero por las dudas x2
import json

@csrf_exempt
def login(request):

     if request.method == "GET":

       v = ""
       return render_to_response('login.html', { 'dato' : v })

     else:

         usuario = request.POST['username']
         contra = request.POST['password']



         r = requests.post("http://api:8000/gen-tk/", data={'username': usuario, 'password': contra})
         jsonData = r.json()


         if r.status_code == 400:

             v = 'Algo esta mal en los campos, alguno esta vacío o las credenciales no coinciden con la base de datos.'
             return render_to_response('login.html', { 'dato' : v })

         elif r.status_code == 200:

             request.session['user'] = usuario
             request.session['token'] = jsonData["token"]
             v = 'De culo salió todo bien.'
             return render_to_response('principal.html', { 'dato' : v })




def logout(request):

    if request.method== 'GET':

        try:

            del request.session['user']
            del request.session['token']


        except KeyError:

            v = 'Logueate antes de intentar hacer algo, gil.'
            return render_to_response('login.html', { 'dato' : v })

        else:

            v = 'Logout ejecutado satisfactoriamente.'
            return render_to_response('login.html', { 'dato' : v })






@csrf_exempt
def principal(request):
    if request.method == 'GET':
        return render_to_response('principal.html')
    else:
        pass
