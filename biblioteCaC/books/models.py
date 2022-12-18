from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
# Category Model
class Category(models.Model):
    development_area= models.CharField(verbose_name="Área del desarrollo", max_length=50, unique=True, blank = False, null = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['development_area']

    def __str__(self):
        return self.development_area
    
# Books Model
class Book(models.Model):
    image = models.ImageField(verbose_name = "Imagen", upload_to = "books-img", blank = False, null = False)
    title = models.CharField(verbose_name="Título", max_length=100, blank = False)
    author = models.CharField(verbose_name="Autor", max_length=100, blank = False)
    genre = models.CharField(verbose_name="Género", max_length=100, blank = False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='get_books', null = True)
    synopsis = RichTextField(verbose_name="Sinopsis", blank = False, null = False)
    order = models.SmallIntegerField(verbose_name="Orden", default=0, blank = False, null = False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def delete(self):
        self.image.delete()
        return super().delete()
    