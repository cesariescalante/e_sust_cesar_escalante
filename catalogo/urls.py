from django.urls import path
from . import views


urlpatterns = [
    path('catalogo_list/', views.platos_list, name='catalogo_list'),


]
