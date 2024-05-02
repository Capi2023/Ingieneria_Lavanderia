from django.db import models
from django.contrib.auth.models import User


class Tarjeta(models.Model):
    nom_titular = models.CharField(max_length=100)
    num_tarjeta = models.CharField(max_length=16)
    fecha_ven_tarjeta = models.DateField()
    nip_tarjeta = models.CharField(max_length=4)

    def __str__(self):
        return self.nom_titular


class ClienteRegistrado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dir_cliente = models.CharField(max_length=200)
    colonia_cliente = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    tel_cliente = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    tarjeta_credito = models.OneToOneField(Tarjeta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class TipoServicio(models.Model):
    cantidad_ropa = models.IntegerField()
    tipo_ropa = models.CharField(max_length=100)
    tipo_servicio = models.CharField(max_length=100)
    detalles_extra = models.CharField(max_length=200)
    dir_entrega = models.CharField(max_length=200)
    cliente = models.ForeignKey(ClienteRegistrado, on_delete=models.CASCADE)
    administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)
    pago = models.ForeignKey('Pago', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_servicio} - {self.tipo_ropa}"


class Ruta(models.Model):
    nom_ruta = models.CharField(max_length=100)
    dir_origen = models.CharField(max_length=200)
    col_origen = models.CharField(max_length=100)
    postal_origen = models.CharField(max_length=10)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE)
    cliente = models.ForeignKey(ClienteRegistrado, on_delete=models.CASCADE)
    lavado_ruta = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, related_name='rutas')
    repartidor = models.ForeignKey('Repartidor', on_delete=models.CASCADE)
    orden_entrega = models.ForeignKey('OrdenEntrega', on_delete=models.CASCADE)
    admin = models.ForeignKey('Administrador', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_ruta


class OrdenEntrega(models.Model):
    nom_ordenentrega = models.CharField(max_length=100)
    fecha_actual = models.DateField()
    hora = models.TimeField()
    cliente = models.ForeignKey(ClienteRegistrado, on_delete=models.CASCADE)
    ruta_orden = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='ordenes_entrega')
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE)
    repartidor = models.ForeignKey('Repartidor', on_delete=models.CASCADE)
    pedidos = models.ForeignKey('Pedidos', on_delete=models.CASCADE)
    admin = models.ForeignKey('Administrador', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_ordenentrega


class Pedidos(models.Model):
    fecha_actual = models.DateField()
    hora = models.TimeField()
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE)
    admin = models.ForeignKey('Administrador', on_delete=models.CASCADE)
    rep = models.ForeignKey('Repartidor', on_delete=models.CASCADE)
    lavado = models.OneToOneField(TipoServicio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(ClienteRegistrado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dir_admin = models.CharField(max_length=200)
    colonia_admin = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    tel_admin = models.CharField(max_length=15)
    direccion_trabajo = models.CharField(max_length=200, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='admin_fotos/', blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Puntuacion(models.Model):
    no_estrellas = models.IntegerField()
    comentarios = models.CharField(max_length=200)
    mejoras = models.CharField(max_length=100)
    cliente = models.ForeignKey(ClienteRegistrado, on_delete=models.CASCADE)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente} - {self.tipo_servicio} - {self.no_estrellas}"


class Transporte(models.Model):
    modelo_trans = models.CharField(max_length=100)
    marca_trans = models.CharField(max_length=100)
    año_trans = models.IntegerField()
    color_trans = models.CharField(max_length=100)
    repartidor = models.ForeignKey('Repartidor', on_delete=models.CASCADE)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE)
    pedidos = models.ForeignKey(Pedidos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo_trans} - {self.marca_trans}"


class Repartidor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dir_repar = models.CharField(max_length=200)
    colonia_repar = models.CharField(max_length=100)
    tel_repar = models.CharField(max_length=15)
    licencia_conducir = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='repartidor_fotos/', blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Sucursal(models.Model):
    nom_sucursal = models.CharField(max_length=100)
    calle_sucursal = models.CharField(max_length=200)
    col_sucursal = models.CharField(max_length=100)
    no_exterior_sucursal = models.CharField(max_length=10)
    no_interior_sucursal = models.CharField(max_length=10)

    def __str__(self):
        return self.nom_sucursal


class Pago(models.Model):
    nom_pago = models.CharField(max_length=100)
    cliente = models.ForeignKey(ClienteRegistrado, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    lavado = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, related_name='pagos')

    def __str__(self):
        return self.nom_pago

