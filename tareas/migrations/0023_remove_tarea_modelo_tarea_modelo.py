# Generated by Django 4.1.3 on 2023-02-09 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0022_remove_producto_cantidad_alter_tarea_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='modelo',
        ),
        migrations.AddField(
            model_name='tarea',
            name='modelo',
            field=models.ManyToManyField(blank=True, null=True, to='tareas.producto'),
        ),
    ]
