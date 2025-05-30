from django.contrib import admin
from .models import Post, Tag, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)