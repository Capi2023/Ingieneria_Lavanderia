# Generated by Django 5.0.4 on 2024-05-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Lavanderia', '0017_alter_tiposervicio_tipo_prenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiposervicio',
            name='tipo_prenda',
            field=models.ManyToManyField(to='App_Lavanderia.tipoprenda'),
        ),
    ]
