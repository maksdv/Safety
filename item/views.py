from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item
from .models import Buscador
from .forms import NameForm
from .forms import Email
from django.core import serializers
import ast
import numpy as np
from django.core.paginator import Paginator

def index(request):
    return render(request, 'item/index.html', {})
    
def presentation(request):
    itemss = Item.objects.all()
    paginator = Paginator(itemss, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request, 'item/presentation.html', {'items': items})


def about(request):
    return render(request, 'item/about.html', {})

def stores(request):

    items_cero = Item.objects.filter(group='0')
    items_uno = Item.objects.filter(group='0-1')
    items_dos_tres = Item.objects.filter(group='2')
    cero_uno=items_cero | items_uno
    
    if request.method == 'POST':
        
        form = NameForm(request.POST)
        
        message = request.session.get('message')
             
        if form.is_valid():
            kk=request.POST.get('edad')
            modo = request.POST.get('modoo')
            
            if int(kk) == 1:
                if modo == 'calidad':
                    cero_uno_calidad=cero_uno.order_by('-score')
                    data = serializers.serialize("json", cero_uno_calidad)
                    request.session['data'] = data
                    
                    return HttpResponseRedirect('/informe', {'form': form,'items': cero_uno_calidad})
                else:
                    
                    cero_uno_precio = cero_uno.order_by('price')
                    data = serializers.serialize("json", cero_uno_precio)
                    ''' pp=ast.literal_eval(data)
                    
                    for cosa in pp:
                        fields = [cosa.get("fields") for cosa in pp] '''
                    request.session['data'] = data
                    return HttpResponseRedirect('/informe',{'form': form,'items': cero_uno_precio})
            if int(kk) == 2:
                if modo == 'precio':
                    items_uno_precio = items_uno.order_by('price')
                    return render(request, 'item/informe.html', {'form': form,'items': items_uno_precio})
                else:
                    items_uno_calidad = items_uno.order_by('-score')
                    return render(request, 'item/informe.html', {'form': form,'items': items_uno_calidad})
            if int(kk) == 3:
                if modo == 'precio':
                    items_dos_precio = items_dos_tres.order_by('price')
                    return render(request, 'item/informe.html', {'form': form,'items': items_dos_precio})
                else:
                    items_dos_calidad = items_dos_tres.order_by('-score')
                    return render(request, 'item/informe.html', {'form': form,'items': items_dos_calidad})
    else:
        form = NameForm()
        
    return render(request, 'item/stores.html', {'form': form})

def informe(request):
    mail = request.POST.get('text')
    kk = request.GET.get('name')
    if request.POST.get('text'):
                send_mail(
                    'Tu lista de sillas está aquí',
                    kk,
                    'maxdv31@gmail.com',
                    [mail],
                    fail_silently=False,
                )

    text = Email()
    data = request.session.get('data')
    pp=ast.literal_eval(data)
                    
    for cosa in pp:
        fields = [cosa.get("fields") for cosa in pp]
        
    
    return render(request, 'item/informe.html', {'text':text, 'data': fields})