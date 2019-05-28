from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item
from .models import Buscador
from .forms import NameForm
import numpy as np

def index(request):
    return render(request, 'item/index.html', {})
    
def presentation(request):
    items = Item.objects.all()
    items_cero = Item.objects.filter(group='0')
    items_uno = Item.objects.filter(group='0-1')
    items_dos_tres = Item.objects.filter(group='2')
    cero_uno=items_cero | items_uno
    
    if request.method == 'POST':

        form = NameForm(request.POST)
        
        if form.is_valid():
            kk=request.POST.get('edad')
            modo = request.POST.get('modoo')
            if int(kk) <= 6:
                if modo == 'calidad':
                    cero_uno_calidad=cero_uno.order_by('-score')
                    return render(request, 'item/presentation.html', {'form': form,'items': cero_uno_calidad})
                else:
                    cero_uno_precio = cero_uno.order_by('price')
                    return render(request, 'item/presentation.html', {'form': form,'items': cero_uno_precio})
            if int(kk) > 6 and int(kk) < 36:
                if modo == 'precio':
                    items_uno_precio = items_uno.order_by('price')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_uno_precio})
                else:
                    items_uno_calidad = items_uno.order_by('-score')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_uno_calidad})
            if int(kk) > 36:
                if modo == 'precio':
                    items_dos_precio = items_dos_tres.order_by('price')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_dos_precio})
                else:
                    items_dos_calidad = items_dos_tres.order_by('-score')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_dos_calidad})

    else:
        form = NameForm()
        
    return render(request, 'item/presentation.html', {'form': form,'items': items_cero, 'itemsCero': items_cero, 'itemsUno': items_uno })


def about(request):
    return render(request, 'item/about.html', {})

def stores(request):
    return render(request, 'item/stores.html', {})

def informe(request):
    return render(request, 'item/informe.html', {})