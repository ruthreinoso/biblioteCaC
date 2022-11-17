from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')
   list_display = ('title', 'order')

admin.site.register(Book, BookAdmin)
