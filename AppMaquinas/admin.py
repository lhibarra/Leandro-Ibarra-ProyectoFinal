from django.contrib import admin

from django.contrib import admin
from AppMaquinas.models import Maquina, Profile, Mensaje

admin.site.register(Profile)
admin.site.register(Mensaje)
admin.site.register(Maquina)

