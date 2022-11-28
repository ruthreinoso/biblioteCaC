from .forms import UserCreationFormEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms


# Create your views here.
class SingUp(CreateView):
    form_class = UserCreationFormEmail
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None):
        form= super(SingUp, self).get_form()
        
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'Dirección de Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Repita la contraseña'})
        return form