from django.contrib import admin
from .models import foto
# Register your models here.

class FotoAdmin(admin.ModelAdmin):
    readonly_fields = ('subido',)


admin.site.register(foto, FotoAdmin)