from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view,permission_classes

from meseros.models import Meseros
from django.db.models import F,Q
from meseros.forms import MeserosForm
from django.views.generic import ListView
from django.core import serializers as ssr
from meseros.serializers import MeserosSerializer
from rest_framework.response import Response


def meseros_list(request):
    # data_context ={
    #     'nombre': 'diego',
    #     'edad':19,
    #     'pais': 'brasil'
    #
    #
    # }
    # mesero = [
    #     {
    #         'nombre': 'cesar',
    #         'edad': 50,
    #         'pais': 'Peru',
    #
    #     },
    #     {
    #         'nombre': 'juan',
    #         'edad': 20,
    #         'pais': 'Peru',
    #     },
    #     {
    #         'nombre': 'eduardo',
    #         'edad': 18,
    #         'pais': 'Ecuador',
    #     },
    #     {
    #         'nombre': 'rosa',
    #         'edad': 21,
    #         'pais': 'venezuela',
    #     },
    #     {
    #         'nombre': 'luz',
    #         'edad': 20,
    #         'pais': 'Peru',
    #     },
    #
    # ]
     #mesero = Meseros.objects.all()
    # mesero = Meseros.objects.order_by('edad') #buscar por
    #mesero = Meseros.objects.all()
    # mesero = Meseros.objects.filter(nombre="pedro").order_by("edad")  #buscar contatenado
    #"""eliminando una fia en la url actualizando y en la base de datos """
    #p = Meseros.objects.filter(id=4)
    #p.delete()
    """colocar la edad a todos que stan el tabla de la base de datos"""
    #Meseros.objects.filter(pais__startswith="Peru").update(edad= 18)

    """utilizando F en las expresiones"""

    #Meseros.objects.filter(edad__gte=18).update(edad=F('edad')+10)

    """consultas complejas"""
    query = Q(pais__startswith="Per") | Q(pais__startswith="br")
    mesero = Meseros.objects.filter(query)

    """consultas negada"""
    #query = Q(pais__startswith="Per") & ~Q(edad=28)
    #mesero = Meseros.objects.filter(query)



    return render(request,'meseros/meseros_list.html', context={'data':mesero})

def meseros_search(request):
    query = request.GET.get('q','')
    result = (
            Q(nombre__icontains=query)
    )

    data_context = Meseros.objects.filter(result).distinct()

    return render(request, 'meseros/meseros_search.html', context={'data': data_context, 'query': query})

def meseros_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    meseros = Meseros.objects.all()
    return render(request, 'meseros/meseros_details.html', context={'data': meseros})

def meseros_create(request):
    #request.method = "POST"
    if request.method == "POST":
        form = MeserosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            pais = form.cleaned_data['pais']
            #try:
            form.save()

                #return redirect('owner_list') #para dirigir a otra lista
            #except:
                #pass
    else:
        form =MeserosForm()

    return render(request, 'meseros/meseros-create.html', {'form': form})


def meseros_delete(request, id_meseros):
    mesero = Meseros.objects.get(id=id_meseros)
    mesero.delete()
    return redirect('meseros_details')

def meseros_edit(request, id_meseros):
    mesero = Meseros.objects.get(id=id_meseros)
    form = MeserosForm(initial={'nombre': mesero.nombre, 'edad':mesero.edad, 'pais':mesero.pais})
    if request.method=='POST':
        form =MeserosForm(request.POST, instance=mesero)
        if form.is_valid():
            form.save()
            return redirect('meseros_details')

    return render(request, 'meseros/meseros_update.html',{'form': form})

class MeserosList(ListView):
    model = Meseros
    template_name ='meseros/meseros_vc.html'


def ListMeserosSerializer(request):
    lista = ssr.serialize('json', Meseros.objects.all(), fields=['nombre', 'pais', 'edad'])
    return HttpResponse(lista, content_type="application/json")

@api_view(['GET', 'POST'])
def meseros_api_view(request):
    if request.method == 'GET':
        queryset = Meseros.objects.all()
        serializers_class = MeserosSerializer(queryset, many=True)

        return Response(serializers_class.data)


    elif request.method=='POST':
        pass


