from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Conteudo
from .forms import ConteudoForm


def conteudoLista(request):
    conteudos = Conteudo.objects.all().order_by('-data_criacao')
    return render(request, 'conteudo/lista.html', {'conteudos': conteudos})


def conteudoView(request, id):
    conteudo = get_object_or_404(Conteudo, pk=id)
    return render(request, 'conteudo/conteudo.html', {'conteudo': conteudo})


def novoBloco(request):
    if request.method == 'POST':
        form = ConteudoForm(request.POST)
        if form.is_valid():
            conteudo = form.save(commit=False)
            conteudo.done = 'doing'
            conteudo.save()
            return redirect('/')
    else:
        form = ConteudoForm()
        return render(request, 'conteudo/addbloco.html', {'form': form})


def editBloco(request, id):
    conteudo = get_object_or_404(Conteudo, pk=id)
    form = ConteudoForm(instance=conteudo)

    if request.method == 'POST':
        form = ConteudoForm(request.POST, instance=conteudo)
        if form.is_valid():
            conteudo.save()
            return redirect('/')
        else:
            return render(request, 'conteudo/editbloco.html', {'form': form, 'conteudo':conteudo})
    else:
        return render(request, 'conteudo/editbloco.html', {'form':form, 'conteudo':conteudo})