from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['image', 'title', 'author', 'genre', 'synopsis', 'order']
        widgets = {
            'title': forms.TextInput(attrs={ 'placeholder':'Titulo'}),
            'author': forms.TextInput(attrs={ 'placeholder':'Autor'}),
            'genre': forms.TextInput(attrs={ 'placeholder':'Género'}),
        }
        labels = {
            'title':'', 'author':'', 'genre':''
        }