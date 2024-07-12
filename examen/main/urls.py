from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='inicio'),
    path('formulario/',views.formulario,name='formulario'),
    path('login/',views.inisesion,name='login'),
    path('salir/',views.salir,name='salir'),
    path('perfil/',views.perfil,name='perfil'),
    path('eliminar/<username>/', views.eliminar, name='eliminar'),
    path('modificar/<username>/',views.modificar,name='modificar'),
    #### items ######
    path('reptiles/',views.reptiles,name='reptiles'),
    path('terrarios/',views.terrarios,name='terrarios'),
    path('alimento/',views.alimento,name='alimento'),
]

    