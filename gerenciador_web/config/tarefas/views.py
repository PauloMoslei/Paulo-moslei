from django.shortcuts import render, get_object_or_404, redirect

from projetos.models import Projeto

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
    projetos = Projeto.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto')
        projeto_selecionado = Projeto.objects.get (pk = projeto_id)
        Tarefa.objects.create(titulo=titulo, descricao=descricao, projeto=projeto_selecionado)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {'projetos': projetos})

#metodos http
#post: envia dados para o servidor
#get: busca dados no servidor 
#put: atualiza recursos existentes
#delete: remove recursos selecionados

def alterar_tarefa(request, tarefa_id):
    projetos = Projeto.objects.all()
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto')
        concluida = request.POST.get('concluida') == 'on' 
        projeto_selecionado = get_object_or_404(Projeto, pk = projeto_id)

      
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluida = concluida
        tarefa.projeto = projeto_selecionado
        
        tarefa.save()
        
        return redirect('lista_tarefas')

    context = {
        'tarefa': tarefa,
        'projetos': projetos,
    }
    return render(request, 'tarefas/form_tarefas.html', context)

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect ('lista_tarefas')
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa})

