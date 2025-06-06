# Generated by Django 5.2.1 on 2025-05-24 01:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catblog', '0010_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='active_post',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catblog.category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='aa-mm-dd', verbose_name='Fecha de Publicación'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='catblog.tag', verbose_name='Etiquetas'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
    ]
