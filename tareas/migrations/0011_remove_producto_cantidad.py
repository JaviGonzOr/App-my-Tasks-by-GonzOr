# Generated by Django 4.1.3 on 2022-12-31 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0010_alter_producto_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
    ]