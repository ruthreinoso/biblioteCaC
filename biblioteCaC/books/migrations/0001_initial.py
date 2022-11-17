# Generated by Django 4.1.1 on 2022-11-15 21:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('genre', models.CharField(max_length=100, verbose_name='Género')),
                ('synopsis', ckeditor.fields.RichTextField(verbose_name='Sinopsis')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'libro',
                'verbose_name_plural': 'libros',
                'ordering': ['title'],
            },
        ),
    ]