# Generated by Django 5.1 on 2024-12-03 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='id_cliente',
        ),
    ]
