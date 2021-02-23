from django.urls import path
from . import views 


urlpatterns = [
    path('', views.conteudolista, name='conteudo-lista'),
    path('conteudo/<int:id>', views.conteudoView, name='conteudo-views'),
]