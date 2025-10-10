from django.urls import path
from . import views #importa nossas views
urlpatterns = [
    path ('', views.listar_tarefas,name= 'lista_tarefas'), #seria /tarefas/
    path ('<int:tarefa_id>/', views.detalhe_tarefa, name = "detalhe_tarefa"),

    #adicionar tarefa
    path('adicionar/' , views.adicionar_tarefa, name= 'adicionar_tarefa'),

    #alterar tarefa
    path('<int:tarefa_id>/alterar/', views.alterar_tarefa, name = 'alterar_tarefa'),

    # excluir tarefa
    path ('<int:tarefa_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa')
]