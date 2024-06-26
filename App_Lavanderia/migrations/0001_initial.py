# Generated by Django 5.0.4 on 2024-05-21 05:14

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio_adicional', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_sucursal', models.CharField(max_length=100)),
                ('calle_sucursal', models.CharField(max_length=200)),
                ('col_sucursal', models.CharField(max_length=100)),
                ('no_exterior_sucursal', models.CharField(max_length=10)),
                ('no_interior_sucursal', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_titular', models.CharField(max_length=100)),
                ('num_tarjeta', models.CharField(max_length=16)),
                ('fecha_ven_tarjeta', models.DateField()),
                ('nip_tarjeta', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_admin', models.CharField(max_length=200)),
                ('colonia_admin', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('tel_admin', models.CharField(max_length=15)),
                ('direccion_trabajo', models.CharField(blank=True, max_length=200, null=True)),
                ('especialidad', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='admin_fotos/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteRegistrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_cliente', models.CharField(max_length=200)),
                ('colonia_cliente', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('tel_cliente', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tarjeta_credito', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.tarjeta')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('CR', 'Creando'), ('EN', 'En espera'), ('AC', 'Aceptado'), ('TE', 'Terminado'), ('RE', 'Rechazado')], default='CR', max_length=2)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('administrador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App_Lavanderia.administrador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.clienteregistrado')),
                ('servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servicios_pedido', to='App_Lavanderia.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(default=datetime.datetime.now)),
                ('monto', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('metodo_pago', models.CharField(default='Tarjeta de Crédito', max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.clienteregistrado')),
                ('pedido', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pago_detalle', to='App_Lavanderia.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_estrellas', models.IntegerField()),
                ('comentarios', models.CharField(max_length=200)),
                ('mejoras', models.CharField(max_length=100)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.administrador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.clienteregistrado')),
                ('tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_repar', models.CharField(max_length=200)),
                ('colonia_repar', models.CharField(max_length=100)),
                ('tel_repar', models.CharField(max_length=15)),
                ('licencia_conducir', models.CharField(max_length=20)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='repartidor_fotos/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ordenentrega', models.CharField(max_length=100)),
                ('fecha_actual', models.DateField()),
                ('hora', models.TimeField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.administrador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.clienteregistrado')),
                ('pedidos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.pedido')),
                ('repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='App_Lavanderia.pedido')),
                ('ropa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.ropa')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ruta', models.CharField(max_length=100)),
                ('dir_origen', models.CharField(max_length=200)),
                ('col_origen', models.CharField(max_length=100)),
                ('postal_origen', models.CharField(max_length=10)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.administrador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.clienteregistrado')),
                ('lavado_ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas', to='App_Lavanderia.pedido')),
                ('orden_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.ordenentrega')),
                ('repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.repartidor')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.sucursal')),
            ],
        ),
        migrations.AddField(
            model_name='ordenentrega',
            name='ruta_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_entrega', to='App_Lavanderia.ruta'),
        ),
        migrations.AddField(
            model_name='ordenentrega',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.sucursal'),
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_trans', models.CharField(max_length=100)),
                ('marca_trans', models.CharField(max_length=100)),
                ('año_trans', models.IntegerField()),
                ('color_trans', models.CharField(max_length=100)),
                ('pedidos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.pedido')),
                ('repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.repartidor')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Lavanderia.sucursal')),
            ],
        ),
    ]
