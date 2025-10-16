from django.urls import path
from . import views 
urlpatterns = [
    path ('', views.listar_projetos,name= 'lista_projetos'), #seria /projetos/
    
]