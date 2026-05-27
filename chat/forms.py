from django import forms
from .models import Canal

class CanalForm(forms.ModelForm):
    class Meta:
        model = Canal
        fields = ('nome', 'descricao', 'tipo')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }
