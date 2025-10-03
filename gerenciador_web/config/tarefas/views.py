from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Tarefa
from django.http import HttpResponse

def listar_tarefas (request):
    tarefas_salvas = Tarefa.objects.all()

    contexto = {
        'minhas_tarefas': tarefas_salvas
    }
    return render(request, 'tarefas/lista.html', contexto)

def detalhe_tarefa (request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk= tarefa_id)
    return render (request, 'tarefas/detalhe.html',{'tarefa':tarefa})