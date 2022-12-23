from django.contrib import admin
from .models import Platos
# Register your models here.

#admin.site.register(Platos)

@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','pais' )