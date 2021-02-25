from django.urls import path
from . import views 


urlpatterns = [
    path('', views.conteudoLista, name='conteudo-lista'),
    path('conteudo/<int:id>', views.conteudoView, name='conteudo-views'),
    path('novobloco/', views.novoBloco, name='novo-bloco'),
    path('edit/<int:id>', views.editBloco, name='edit-bloco'),
    path('delete/<int:id>', views.deleteBloco, name='delete-bloco'),
]