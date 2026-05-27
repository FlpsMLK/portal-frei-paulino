from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'slug', 'categoria', 'tags', 'empresa', 'conteudo', 'imagem_capa', 'status')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: google, entrevista, tech'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 12}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('conteudo',)
        widgets = {'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escreva seu comentário...'})}
        labels = {'conteudo': 'Comentário'}

class BuscaForm(forms.Form):
    q = forms.CharField(label='Busca', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar posts...'}))
