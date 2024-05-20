from django.contrib import admin
from django.urls import path, include
from App_Lavanderia import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    # Clientes
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('agregar_tarjeta/', views.agregar_tarjeta, name='agregar_tarjeta'),
    path('editar_tarjeta/<int:tarjeta_id>/', views.editar_tarjeta, name='editar_tarjeta'),
    path('index/cliente/', views.index_cliente, name='index_cliente'),
    path('miembros/', include('miembros.urls')),
    path('miembros/', include('django.contrib.auth.urls')),
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedido/nuevo/', views.crear_pedido, name='crear_pedido'),
    path('pedido/editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('pedido_enviado/', views.pedido_enviado, name='pedido_enviado'),
    path('pedidos_en_proceso/', views.pedidos_en_proceso, name='pedidos_en_proceso'),
    path('realizar_pago_cliente/<int:pedido_id>/', views.realizar_pago_cliente, name='realizar_pago_cliente'),
    # Administrador
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('actualizar_cliente/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('actualizar_repartidor/<int:repartidor_id>/', views.actualizar_repartidor, name='actualizar_repartidor'),
    path('crear_repartidor/', views.crear_repartidor, name='crear_repartidor'),
    path('cliente-creado/', views.cliente_creado, name='cliente_creado'),
    path('ver-usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('gestionar_pedido/<int:pedido_id>/', views.gestionar_pedido, name='gestionar_pedido'),
    path('cambiar_estado_pedido/<int:pedido_id>/<str:nuevo_estado>/', views.cambiar_estado_pedido, name='cambiar_estado_pedido'),
    path('realizar_pago/<int:pedido_id>/', views.realizar_pago, name='realizar_pago'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

