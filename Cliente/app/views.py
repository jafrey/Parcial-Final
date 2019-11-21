from django.shortcuts import render, render_to_response

from django.contrib.auth.hashers import make_password

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



@csrf_exempt
def altaCancion(request):

    if request.method == "GET":

        return render_to_response('alta.html')

    else:

        nom_cancion = request.POST['nom_cancion']
        desc_cancion = request.POST['desc_cancion']


        try:

            r = requests.post("http://api:8000/canciones/", data={'nom_cancion': nom_cancion, 'desc_cancion': desc_cancion}, headers={'Authorization':'Token ' + request.session['token']})

        except KeyError:

            estado = 'No tenes permiso, te mando a los pacos al toque gil.'
            return render_to_response('alta.html', { 'estado' : estado })

        else:

            estado = r.status_code

            if estado == 201:
                estado = 'Cancion creada, sos un crack papaaaaaaaaa.'
                return render_to_response('alta.html', { 'estado' : estado })
            elif estado == 400:
                estado = 'Algo estaba mal, pone bien las cosas boludo.'
                return render_to_response('alta.html', { 'estado' : estado })


@csrf_exempt
def bajaCancion(request):

    if request.method == "GET":

        return render_to_response('baja.html')

    else:

        pk = request.POST['pk']



        try:

            r = requests.delete("http://api:8000/canciones/" + pk, headers={'Authorization':'Token ' + request.session['token']})

        except KeyError:

            estado = 'No tenes permiso, te mando a los pacos al toque gil.'
            return render_to_response('baja.html', { 'estado' : estado })

        else:

            estado = r.status_code

            if estado == 204:
                estado = 'Cancion eliminada, que cagada.'
                return render_to_response('baja.html', { 'estado' : estado })
            elif estado == 404:
                estado = 'No existe esa rola.'
                return render_to_response('baja.html', { 'estado' : estado })
            elif estado == 405:
                estado = 'Pone algo, jeropa.'
                return render_to_response('baja.html', { 'estado' : estado })


@csrf_exempt
def modCancion(request):

    if request.method == "GET":

        return render_to_response('mod.html')

    else:

        id = request.POST['id']
        nom_cancion = request.POST['nom_cancion']
        desc_cancion = request.POST['desc_cancion']


        try:

            r = requests.put("http://api:8000/canciones/" + id + "/", data={'nom_cancion': nom_cancion, 'desc_cancion': desc_cancion}, headers={'Authorization':'Token ' + request.session['token']})

        except KeyError:

            estado = 'No tenes permiso, te mando a los pacos al toque gil.'
            return render_to_response('mod.html', { 'estado' : estado })

        else:

            estado = r.status_code

            if estado == 200:
                estado = 'Cancion modificada satisfactoriamente.'
                return render_to_response('mod.html', { 'estado' : estado })
            elif estado == 400:
                estado = 'Algo estaba mal, pone bien las cosas boludo.'
                return render_to_response('mod.html', { 'estado' : estado })
            elif estado == 404:
                estado = 'Cancion a modificar no encontrada.'
                return render_to_response('mod.html', { 'estado' : estado })


@csrf_exempt
def listaCancion(request):

    if request.method == "POST":

        return render_to_response('lista.html')

    else:

            try:

                r = requests.get("http://api:8000/canciones/", headers={'Authorization':'Token ' + request.session['token']})

            except KeyError:

                estado = 'No tenes permiso, te mando a los pacos al toque gil.'
                return render_to_response('lista.html', { 'estado' : estado })

            else:

                estado = r.status_code

            if estado == 200:

                jsonData = r.json()
                return render_to_response('lista.html', { 'items' : jsonData })


            else:
                estado = 'Hubo algún error.'
                return render_to_response('lista.html', { 'estado' : estado })

@csrf_exempt
def altaUsuario(request):

    if request.method == "GET":

        return render_to_response('ualta.html')

    else:

        usuario = request.POST['usuario']
        contra = request.POST['contraseña']
        contraHashed = make_password(contra)

        try:

            r = requests.post("http://api:8000/users/", data={'username': usuario, 'password': contraHashed}, headers={'Authorization':'Token ' + request.session['token']})

        except KeyError:

            estado = 'No tenes permiso, te mando a los pacos al toque gil.'
            return render_to_response('ualta.html', { 'estado' : estado })

        else:

            estado = r.status_code

            if estado == 201:
                estado = 'Usuario creado, sos un crack papaaaaaaaaa.'
                return render_to_response('ualta.html', { 'estado' : estado })
            elif estado == 400:
                estado = 'Ese usuario ya esta creado zapayo o alguno de los campos esta mal.'
                return render_to_response('ualta.html', { 'estado' : estado })
