from django import forms
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteRegistrado
        fields = ['user', 'dir_cliente', 'colonia_cliente', 'codigo_postal', 'tel_cliente', 'fecha_nacimiento', 'tarjeta_credito']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_superuser=False).exclude(Q(clienteregistrado__isnull=False) | Q(repartidor__isnull=False))



class RepartidorForm(forms.ModelForm):
    class Meta:
        model = Repartidor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_superuser=False).exclude(Q(clienteregistrado__isnull=False) | Q(repartidor__isnull=False))



class ClienteEditForm(forms.ModelForm):
    class Meta:
        model = ClienteRegistrado
        exclude = ['user'] 


class TipoServicioForm(forms.ModelForm):
    cliente = forms.CharField(widget=forms.HiddenInput())
    dir_entrega = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = TipoServicio
        fields = ['cantidad_ropa', 'tipo_ropa', 'tipo_servicio', 'detalles_extra']

    def __init__(self, *args, cliente=None, **kwargs):
        super().__init__(*args, **kwargs)
        if cliente:
            self.fields['cliente'].initial = cliente.user.pk  # Corregido aquí
            self.fields['dir_entrega'].initial = cliente.dir_cliente


class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['nom_titular', 'num_tarjeta', 'fecha_ven_tarjeta', 'nip_tarjeta']


from django import forms
from .models import Pedidos

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['fecha_actual', 'hora', 'sucursal', 'admin', 'rep', 'lavado', 'cliente']

