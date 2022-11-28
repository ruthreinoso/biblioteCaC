from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Book(models.Model):
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects", blank = False, null = False)
    title = models.CharField(verbose_name="Título", max_length=100, blank = False, null = False)
    author = models.CharField(verbose_name="Autor", max_length=100, blank = False, null = False)
    genre = models.CharField(verbose_name="Género", max_length=100, blank = False, null = False)
    synopsis = RichTextField(verbose_name="Sinopsis", blank = False, null = False)
    order = models.SmallIntegerField(verbose_name="Orden", default=0, blank = False, null = False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def delete(self):
        self.image.delete()
        return super().delete()
    