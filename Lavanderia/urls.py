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
    path('enviar_pedido/', views.enviar_pedido, name='enviar_pedido'),
    path('pedido_enviado/', views.pedido_enviado, name='pedido_enviado'),
    path('proceso-pedido/', views.pedidos_en_proceso, name='pedidos_en_proceso'),
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)