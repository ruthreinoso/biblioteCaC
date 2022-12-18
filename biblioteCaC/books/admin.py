from django.contrib import admin
from .models import Book, Category


# Register your models here.
# Category
class CategoryAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')
   list_display = ('development_area', 'created')
   
admin.site.register(Category, CategoryAdmin)
 
#Book   
class BookAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')
   list_display = ('title', 'author', 'category', 'created', 'updated')
   list_filter = ('category',)

admin.site.register(Book, BookAdmin)
