from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Categoría: " + self.name
    

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="Título")
    content = models.TextField(max_length=1000, verbose_name="Contenido")
    publish_date = models.DateField(default=timezone.now, verbose_name="Fecha de Publicación", help_text="aa-mm-dd")
    active_post = models.BooleanField(default=True, verbose_name="Activo")
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name="Categoría")
    tags = models.ManyToManyField(Tag, verbose_name="Etiquetas")

    def __str__(self):
        return self.title
