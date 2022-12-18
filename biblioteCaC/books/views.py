from .models import Book, Category
from .forms import BookForm
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Create your views here.
class BookList(ListView):
    model = Book
    
class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class CategoryView(ListView):
    template_name = 'books/category.html'
    context_object_name = 'category'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        return category

@method_decorator(staff_member_required, name='dispatch')
class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')

@method_decorator(staff_member_required, name='dispatch')    
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('books:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:books')    