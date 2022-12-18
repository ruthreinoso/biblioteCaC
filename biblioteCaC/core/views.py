from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"

class ContactPageView(TemplateView):
    template_name = 'core/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context