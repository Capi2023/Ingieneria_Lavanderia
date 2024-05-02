from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .models import *


def landing(request):
    return render(request, 'landing_page.html')


def index(request):
    return render(request, 'index.html')


def index_cliente(request):
    return render(request, 'index_cliente.html')


def ver_usuarios(request):
    clientes = ClienteRegistrado.objects.all()
    repartidores = Repartidor.objects.all()
    admin = Administrador.objects.all()
    usuarios = User.objects.all()
    return render(request, 'ver_clientes.html', {'clientes': clientes, 'usuarios': usuarios, 'repartidores': repartidores, 'admin': admin})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_usuarios')  # Redirige a la vista de ver clientes
    else:
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')  # Redirige a la vista de ver clientes
    else:
        form = ClienteForm()
    return render(request, 'crear_cliente.html', {'form': form})


def crear_repartidor(request):
    if request.method == 'POST':
        form = RepartidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_repartidor')
    else:
        form = RepartidorForm()
    return render(request, 'crear_repartidor.html', {'form': form})


def actualizar_repartidor(request, repartidor_id):
    repartidor = get_object_or_404(Repartidor, pk=repartidor_id)
    if request.method == 'POST':
        form = RepartidorForm(request.POST, instance=repartidor)
        if form.is_valid():
            form.save()
            return redirect('ver_usuario', repartidor_id=repartidor_id)
    else:
        form = RepartidorForm(instance=repartidor)
    return render(request, 'actualizar_repartidor.html', {'form': form, 'repartidor': repartidor})


def cliente_creado(request):
    return render(request, 'cliente_creado.html')


def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteRegistrado, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_usuario', cliente_id=cliente_id)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'actualizar_cliente.html', {'form': form, 'cliente': cliente})


def enviar_pedido(request):
    cliente = ClienteRegistrado.objects.get(user=request.user)
    administrador = Administrador.objects.first()  # Obtener el primer administrador
    if request.method == 'POST':
        form = TipoServicioForm(request.POST, cliente=cliente)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = cliente
            pedido.dir_entrega = cliente.dir_cliente
            pedido.administrador = administrador  # Asignar el primer administrador
            pedido.save()
            return redirect('index_cliente')
    else:
        form = TipoServicioForm(cliente=cliente)

    return render(request, 'enviar_pedido.html', {'form': form})


def pedido_enviado(request):
    return render(request, 'pedido_enviado.html')


def ver_pedidos(request):
    tiposervicios_sin_pedido = TipoServicio.objects.filter(pedidos__isnull=True)
    tiposervicios_con_pedido = TipoServicio.objects.filter(pedidos__isnull=False)
    
    if request.method == 'POST':
        decision = request.POST.get('decision')
        tipo_servicio_id = request.POST.get('tipo_servicio_id')
        
        if decision == 'aceptar':
            tipo_servicio = TipoServicio.objects.get(id=tipo_servicio_id)
            # Obtener el primer registro de Sucursal, Admin y Repartidor
            primera_sucursal = Sucursal.objects.first()
            primer_admin = Administrador.objects.first()
            primer_repartidor = Repartidor.objects.first()
            
            # Crear un nuevo pedido
            nuevo_pedido = Pedidos.objects.create(
                fecha_actual=timezone.now().date(),
                hora=timezone.now().time(),
                cliente=tipo_servicio.cliente,
                sucursal=primera_sucursal,
                admin=primer_admin,
                rep=primer_repartidor,
                lavado=tipo_servicio,
            )
            # Actualizar el estado del tipo de servicio
            tipo_servicio.estado = 'Aceptado'
            tipo_servicio.save()
            # Redirigir a la vista para ver los pedidos
            return redirect('ver_pedidos')
        
        elif decision == 'rechazar':
            # Eliminar el tipo de servicio
            TipoServicio.objects.filter(id=tipo_servicio_id).delete()
            # Redirigir a la vista para ver los pedidos
            return redirect('ver_pedidos')

    return render(request, 'ver_pedidos.html', {'tiposervicios_sin_pedido': tiposervicios_sin_pedido, 'tiposervicios_con_pedido': tiposervicios_con_pedido})


def gestionar_pedido(request, pedido_id):
    pedido = Pedidos.objects.get(id=pedido_id)
    tipo_servicio_form = TipoServicioForm(instance=pedido.lavado)  # Crear una instancia del formulario con el TipoServicio asociado al pedido
    
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('ver_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    
    return render(request, 'gestionar_pedido.html', {'form': form, 'tipo_servicio_form': tipo_servicio_form})


def perfil(request):
    cliente = ClienteRegistrado.objects.get(user=request.user)
    return render(request, 'perfil.html', {'cliente': cliente})


def editar_perfil(request):
    cliente = ClienteRegistrado.objects.get(user=request.user)
    if request.method == 'POST':
        form = ClienteEditForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ClienteEditForm(instance=cliente)
    return render(request, 'editar_perfil.html', {'form': form})


def agregar_tarjeta(request):
    cliente = ClienteRegistrado.objects.get(user=request.user)
    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.cliente = cliente
            tarjeta.save()
            return redirect('perfil')
    else:
        form = TarjetaForm()
    return render(request, 'agregar_tarjeta.html', {'form': form})


def editar_tarjeta(request, tarjeta_id):
    cliente = request.user.clienteregistrado
    tarjeta = cliente.tarjeta_credito
    
    if request.method == 'POST':
        form = TarjetaForm(request.POST, instance=tarjeta)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = TarjetaForm(instance=tarjeta)
    
    return render(request, 'editar_tarjeta.html', {'form': form})


def pedidos_en_proceso(request):
    # Obtener el cliente actual
    cliente = request.user.clienteregistrado
    # Obtener los pedidos en proceso del cliente actual
    pedidos_en_proceso = Pedidos.objects.filter(cliente=cliente)
    return render(request, 'proceso_pedido.html', {'pedidos_en_proceso': pedidos_en_proceso})



