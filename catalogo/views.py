from django.shortcuts import render

# Create your views here.

def platos_list(request):
    data_context ={
        'nombre': 'carapulcra',
        'precio':50,
        'pais': 'Peru',



    }

    return render(request, 'catalogo_list.html', context={'data': data_context})