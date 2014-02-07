from django.contrib import admin
from web2.models import *


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ('orden', 'nombre', 'slug', 'titulo')


class PaginaAdmin(admin.ModelAdmin):
    model = Pagina
    list_display = ('titulo', 'slug')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Pagina, PaginaAdmin)