from django.urls import path
from . import views


urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_search/', views.meseros_search, name='meseros_search'),
    path('meseros_details/', views.meseros_details, name='meseros_details'),
    path('meseros_create/', views.meseros_create, name='meseros_create'),
    path('meseros_delete/', views.meseros_delete, name='meseros_delete'),
    path('meseros_edit/<int:id_meseros>/', views.meseros_edit, name='meseros_edit'),

    path('meseros_list_serializer/', views.ListMeserosSerializer, name='meseros_list_srr'),

    path('meseros_list_drf_def/', views.meseros_api_view, name='meseros_list_rf_def'),

]
