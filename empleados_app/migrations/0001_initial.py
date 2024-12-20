# Generated by Django 5.1 on 2024-11-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre_emp', models.CharField(max_length=100)),
                ('apellidos_emp', models.CharField(max_length=200)),
                ('telefono_emp', models.CharField(max_length=20)),
                ('email_emp', models.EmailField(max_length=100)),
                ('puesto', models.CharField(max_length=100)),
                ('id_cliente', models.IntegerField()),
            ],
        ),
    ]
