from django import forms
from .models import Conteudo


class ConteudoForm(forms.ModelForm):

    
    class Meta:
        model = Conteudo
        fields = ('titulo', 'descricao')