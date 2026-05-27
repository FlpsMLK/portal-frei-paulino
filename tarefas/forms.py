from django import forms
from .models import Tarefa, Entrega

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('titulo', 'descricao', 'turma', 'prazo', 'arquivo_enunciado', 'criterios', 'status')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'turma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 3A ou todas'}),
            'prazo': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'criterios': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ('arquivo', 'comentario')
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações sobre sua entrega...'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ('nota', 'feedback')
        widgets = {
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
