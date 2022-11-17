from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class BookList(ListView):
    model = Book
    
class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')
    
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('books:update', args=[self.object.id]) + '?ok'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:books')    