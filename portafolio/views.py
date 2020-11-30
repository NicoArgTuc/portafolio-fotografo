from django.shortcuts import render
from django.http import request, HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import foto

def index(request):
    excepcion = 'Principal'
    excepcion2 = 'a%'
    excepcion3 = 'b%'
    perfil = foto.objects.get(nombre="foto de perfil")
    principal = foto.objects.get(nombre=excepcion)
    galeria = foto.objects.raw('SELECT * FROM portafolio_foto WHERE NOT nombre = %s AND nombre LIKE %s', [excepcion, excepcion2])
    galeria2 = foto.objects.raw('SELECT * FROM portafolio_foto WHERE NOT nombre = %s AND nombre LIKE %s', [excepcion, excepcion3])
    
    return render(request, 'portafolio/portafolio.html', {'galeria': galeria, 'galeria2': galeria2, 'principal': principal, 'perfil': perfil})

def envio_de_correo(request):
    if request.method == 'POST':
        asunto = "Mensaje para Regina Falange"
        mensaje = request.POST['mensaje'] + "[ emisor: " + request.POST['email'] + " nombre: " + request.POST['nombre'] + "]"
        print("mensaje recibido")
        print(mensaje)
        email_from = settings.EMAIL_HOST_USER
        email_to = ['@gmail.com']
        send_mail(asunto, mensaje, email_from, email_to)
        response = JsonResponse({'estado': 'enviado'})
        return HttpResponse(response)
    else: 
        response = JsonResponse({'estado': 'NO enviado'})
        return HttpResponse(response)