from django.shortcuts import render, get_object_or_404, redirect

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

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo= titulo, descricao= descricao)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/form_tarefa.html')

#metodos http
#post: envia dados para o servidor
#get: busca dados no servidor 
#put: atualiza recursos existentes
#delete: remove recursos selecionados

