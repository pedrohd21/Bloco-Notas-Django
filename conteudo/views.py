from django.shortcuts import render
# from django.http import HttpResponse
from .models import Conteudo
from django.shortcuts import get_object_or_404


def conteudolista(request):
    conteudos = Conteudo.objects.all()
    return render(request, 'conteudo/lista.html', {'conteudos': conteudos})


def conteudoView(request, id):
    conteudo = get_object_or_404(Conteudo, pk=id)
    return render(request, 'conteudo/conteudo.html', {'conteudo': conteudo})
