from django.urls import path
from . import views


urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_create/', views.platos_create, name='platos_create'),
    path('platos_edit/<int:id_meseros>/', views.platos_edit, name='platos_edit'),
    path('platos_list_serializer/', views.ListPlatosSerializer, name='platos_list_srr'),
    path('platos_details/', views.platos_details, name='platos_details'),
    path('platos_list_drf_def/', views.platos_api_view, name='platos_list_rf_def'),

]