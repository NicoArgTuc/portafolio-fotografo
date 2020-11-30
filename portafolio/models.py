from django.db import models

# Create your models here.
class foto (models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'galeria')
    subido = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'

    def __str__(self):
        return self.nombre
