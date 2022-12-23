from django.shortcuts import render
from platos.forms import PlatosForm
# Create your views here.
from platos.models import Platos
from django.http import HttpResponse
from django.core import serializers as ssr
from platos.serializers import PlatosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

def platos_list(request):
    # data_context ={
    #     'nombre': 'carapulcra',
    #     'precio':50,


    #
    # }
    #
    # plato =[
    #     {
    #         'nombre': 'carapulcra',
    #         'precio':50,
    #         'pais': 'Peru',
    #
    #       },
    #     {
    #         'nombre': 'ceviche',
    #         'precio': 60,
    #         'pais': 'Peru',
    #     },
    #     {
    #         'nombre': 'arroz con pollo',
    #         'precio': 50,
    #         'pais': 'Ecuador',
    #     },
    #     {
    #         'nombre': 'aji de gallina',
    #         'precio': 30,
    #         'pais': 'venezuela',
    #     },
    #     {
    #         'nombre': 'lomo saltado',
    #         'precio': 70,
    #         'pais': 'Peru',
    #     },
    #
    #
    #
    #
    # ]
    #
    # p = Platos(nombre="rosmery", precio=25)
    # p.save()
    #
    # p.nombre = "Carla"
    # p.save()

    plato = Platos.objects.all()

    return render(request,'platos_list.html', context={'data':plato})


def ListPlatosSerializer(request):
    lista = ssr.serialize('json', Platos.objects.all(), fields=['nombre', 'precio', 'pais'])
    return HttpResponse(lista, content_type="application/json")

def platos_create(request):
    #request.method = "POST"
    if request.method == "POST":
        form = PlatosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            pais = form.cleaned_data['pais']
            #try:
            form.save()

                #return redirect('owner_list') #para dirigir a otra lista
            #except:
                #pass
    else:
        form =PlatosForm()

    return render(request, 'platos_create.html', {'form': form})

def platos_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    plato = Platos.objects.all()
    return render(request, 'platos_details.html', context={'data': plato})


def platos_edit(request, id_platos):
    plato = Platos.objects.get(id=id_platos)
    form = PlatosForm(initial={'nombre': platos.nombre, 'edad':platos.precio, 'pais':platos.pais})
    if request.method=='POST':
        form =PlatosForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('platos_details')

    return render(request, 'platos_details.html',{'form': form})

@api_view(['GET', 'POST'])
def platos_api_view(request):
    if request.method == 'GET':
        queryset = Platos.objects.filter(pais='Peru') # PLATOS DE PERU
        serializers_class = PlatosSerializer(queryset, many=True)

        return Response(serializers_class.data)


    elif request.method=='POST':
        pass