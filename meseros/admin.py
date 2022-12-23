from django.contrib import admin
from .models import Meseros
# Register your models here.

#admin.site.register(Meseros)
@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'pais' )
    search_fields = ('nombre', 'pais')  # Agrega un campo de búsqueda en la parte adminsitrativa
    fields = ('nombre', 'edad', 'pais')  # Ocultar o visualizar los campos al momento de crear un registro

