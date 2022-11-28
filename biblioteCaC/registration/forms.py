from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserCreationFormEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obligatorio. Debe ser válido y con un máximo de 254 caracteres.")
    
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya se encuentra registrado, intente con uno nuevo.")
        return email