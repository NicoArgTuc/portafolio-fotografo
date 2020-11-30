from django.urls import path

from . import views

urlpatterns = [
    path('portafolio/', views.index, name="index"),
    path('envio/', views.envio_de_correo, name="envio de correo"),
]
