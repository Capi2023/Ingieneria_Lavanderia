# Generated by Django 5.0.4 on 2024-05-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Lavanderia', '0013_tiposervicio_tipo_prenda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiposervicio',
            name='tipo_prenda',
            field=models.CharField(choices=[('Pantalones', 'Pantalones'), ('Calzones', 'Calzones'), ('Calcetines', 'Calcetines'), ('Blusas', 'Blusas'), ('Sombreros', 'Sombreros'), ('Camisetas', 'Camisetas'), ('Faldas', 'Faldas'), ('Vestidos', 'Vestidos'), ('Chaquetas', 'Chaquetas'), ('Camisas', 'Camisas'), ('Suéteres', 'Suéteres'), ('Shorts', 'Shorts'), ('Sacos', 'Sacos')], max_length=100),
        ),
    ]