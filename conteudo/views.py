from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Conteudo
from .forms import ConteudoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib.auth.decorators import login_required


@login_required
def conteudoLista(request):
    search = request.GET.get('search')
    if search:
        conteudos = Conteudo.objects.filter(titulo=search, user=request.user)
    else:
        conteudos_lista = Conteudo.objects.all().order_by('-data_criacao').filter(user=request.user)
        paginator = Paginator(conteudos_lista, 10)
        page = request.GET.get('page')
        conteudos = paginator.get_page(page)

    return render(request, 'conteudo/lista.html', {'conteudos': conteudos})


@login_required
def conteudoView(request, id):
    conteudo = get_object_or_404(Conteudo, pk=id)
    return render(request, 'conteudo/conteudo.html', {'conteudo': conteudo})


@login_required
def novoBloco(request):
    if request.method == 'POST':
        form = ConteudoForm(request.POST)

        if form.is_valid():
            conteudo = form.save(commit=False)
            conteudo.done = 'doing'
            conteudo.user = request.user
            conteudo.save()

            messages.info(request, 'Bloco criado com sucesso.')
            return redirect('/')
    else:
        form = ConteudoForm()
        return render(request, 'conteudo/addbloco.html', {'form': form})


@login_required
def editBloco(request, id):
    conteudo = get_object_or_404(Conteudo, pk=id)
    form = ConteudoForm(instance=conteudo)

    if request.method == 'POST':
        form = ConteudoForm(request.POST, instance=conteudo)
        if form.is_valid():
            conteudo.save()
            messages.info(request, 'Nota Editada com sucesso.')
            return redirect('/')
        else:
            return render(request, 'conteudo/editbloco.html', {'form': form, 'conteudo':conteudo})
    else:
        return render(request, 'conteudo/editbloco.html', {'form':form, 'conteudo':conteudo})


@login_required
def deleteBloco(request, id):
    conteudo = get_object_or_404(Conteudo, pk=id)
    conteudo.delete()
    
    messages.info(request, 'Bloco deletado com sucesso.')
    return redirect('/')


