# Generated by Django 5.0.4 on 2024-05-21 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Lavanderia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='total',
        ),
    ]
