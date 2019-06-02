from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item
from .models import Buscador
from .forms import NameForm
import numpy as np
from django.core.paginator import Paginator

def index(request):
    return render(request, 'item/index.html', {})
    
def presentation(request):
    itemss = Item.objects.all()
    paginator = Paginator(itemss, 4)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    items_cero = Item.objects.filter(group='0')
    items_uno = Item.objects.filter(group='0-1')
    items_dos_tres = Item.objects.filter(group='2')
    cero_uno=items_cero | items_uno
    
    if request.method == 'POST':

        form = NameForm(request.POST)
        
        if form.is_valid():
            kk=request.POST.get('edad')
            modo = request.POST.get('modoo')
            if int(kk) == 1:
                if modo == 'calidad':
                    cero_uno_calidad=cero_uno.order_by('-score')
                    paginator = Paginator(cero_uno_calidad, 4)
                    page = request.GET.get('page')
                    cero_uno_calidad_p = paginator.get_page(page)
                    return render(request, 'item/stores.html', {'form': form,'items': cero_uno_calidad_p})
                else:
                    cero_uno_precio = cero_uno.order_by('price')
                    paginator = Paginator(cero_uno_precio, 4)
                    page = request.GET.get('page')
                    cero_uno_precio_p = paginator.get_page(page)
                    return render(request, 'item/stores.html', {'form': form,'items': cero_uno_precio_p})
            if int(kk) == 2:
                if modo == 'precio':
                    items_uno_precio = items_uno.order_by('price')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_uno_precio})
                else:
                    items_uno_calidad = items_uno.order_by('-score')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_uno_calidad})
            if int(kk) == 3:
                if modo == 'precio':
                    items_dos_precio = items_dos_tres.order_by('price')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_dos_precio})
                else:
                    items_dos_calidad = items_dos_tres.order_by('-score')
                    return render(request, 'item/presentation.html', {'form': form,'items': items_dos_calidad})

    else:
        form = NameForm()
        
    return render(request, 'item/presentation.html', {'form': form,'items': items, 'itemsCero': items_cero, 'itemsUno': items_uno })


def about(request):
    return render(request, 'item/about.html', {})

def stores(request):
    return render(request, 'item/stores.html', {})

def informe(request):
    return render(request, 'item/informe.html', {})