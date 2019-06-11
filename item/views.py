from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item
from .models import Buscador
from .forms import NameForm
from .forms import EmailForm
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
    items_unn = Item.objects.filter(group='0-1')
    items_un = Item.objects.filter(group='1')
    items_dos_tres = Item.objects.filter(group='2')
    items_dos_tres_no_isofix = items_dos_tres.filter(isofix='no')
    items_uno = items_unn | items_un

    cero_uno=items_cero | items_unn
    
    if request.method == 'POST':
        
        form = NameForm(request.POST)
        
        message = request.session.get('message')
             
        if form.is_valid():
            kk=request.POST.get('edad')
            modo = request.POST.get('modoo')
            isofix = request.POST.get('isofix')
            
            if int(kk) == 1:
                if modo == 'calidad':
                    cero_uno_calidad=cero_uno.order_by('-score')
                    data = serializers.serialize("json", cero_uno_calidad)
                    request.session['data'] = data
                    return HttpResponseRedirect('/informe', {})
                else:
                    cero_uno_precio = cero_uno.order_by('price')
                    data = serializers.serialize("json", cero_uno_precio)
                    request.session['data'] = data
                    return HttpResponseRedirect('/informe',{})
            if int(kk) == 2:
                if modo == 'precio':
                    items_uno_precio = items_uno.order_by('price')
                    if isofix == 'si':
                        data = serializers.serialize("json", items_uno_precio)
                        request.session['data'] = data
                    else:
                        items_uno_no_isofix = items_uno_precio.filter(isofix='no')
                        data = serializers.serialize("json", items_uno_no_isofix)
                        request.session['data'] = data
                    return HttpResponseRedirect('/informe',{})
                else:
                    items_uno_calidad = items_uno.order_by('-score')
                    if isofix == 'si':
                        data = serializers.serialize("json", items_uno_calidad)
                        request.session['data'] = data
                    else:
                        items_uno_calidad_noisofix = items_uno_calidad.filter(isofix='no')
                        data = serializers.serialize("json", items_uno_calidad_noisofix)
                        request.session['data'] = data
                    return HttpResponseRedirect('/informe',{})
            if int(kk) == 3:
                if modo == 'precio':
                    items_dos_precio = items_dos_tres.order_by('price')
                    data = serializers.serialize("json", items_dos_precio)
                    request.session['data'] = data
                    return HttpResponseRedirect('/informe', {})
                else:
                    items_dos_calidad = items_dos_tres.order_by('-score')
                    data = serializers.serialize("json", items_dos_calidad)
                    request.session['data'] = data
                    return HttpResponseRedirect('/informe', {})
    else:
        form = NameForm()
        
    return render(request, 'item/stores.html', {'form': form})

def informe(request):
    if request.GET.get('go'):
        return HttpResponseRedirect('/stores', {})

    mail = request.POST.get('text')
    kk = request.GET.get('name')
    data = request.session.get('data')
    pp=ast.literal_eval(data)
    namess=''

    for it in pp:
        namess += it.get("fields").get("name")+", "

    names = "Aquí está tu lista de sillas que nos pediste: "+namess[:len(namess) - 2]

    for it in pp:
        fields = [it.get("fields") for it in pp]

    paginator = Paginator(fields, 3)
    page = request.GET.get('page')
    fields = paginator.get_page(page)

    if request.POST.get('text'):
                send_mail(
                    'Tal y como prometimos.',
                    names,
                    'maxdv31@gmail.com',
                    [mail],
                    fail_silently=False,
                )
                return HttpResponseRedirect('/agrad', {})

    text = EmailForm()
    
                    
    

    return render(request, 'item/informe.html', {'text':text, 'data': fields})

def agrad(request):
    return render(request, 'item/agrad.html', {})
   