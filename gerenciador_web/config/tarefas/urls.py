from django.urls import path
from . import views #importa nossas views
urlpatterns = [
    path ('', views.listar_tarefas,name= 'lista_tarefas'), #seria /tarefas/
    path ('<int:tarefa_id>/', views.detalhe_tarefa, name = "detalhe_tarefa"),

    #Adicionar tarefas
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
]
