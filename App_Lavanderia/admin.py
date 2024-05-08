from django.contrib import admin
from .models import ClienteRegistrado, TipoServicio, Ruta, OrdenEntrega, Pedidos, Administrador, Puntuacion, Tarjeta, Transporte, Repartidor, Sucursal, Pago, TipoPrenda

# Registrar los modelos en el panel de administración
admin.site.register(ClienteRegistrado)
admin.site.register(TipoServicio)
admin.site.register(Ruta)
admin.site.register(OrdenEntrega)
admin.site.register(Pedidos)
admin.site.register(Administrador)
admin.site.register(Puntuacion)
admin.site.register(Tarjeta)
admin.site.register(Transporte)
admin.site.register(Repartidor)
admin.site.register(Sucursal)
admin.site.register(Pago)
admin.site.register(TipoPrenda)
