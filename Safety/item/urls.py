from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('presentation', views.presentation, name='presentation'),
    path('about', views.about, name='about' ),
    path('stores/', views.stores, name="stores"),
    path('informe/', views.informe, name="informe"),
    path('agrad/', views.agrad, name="agrad")
]