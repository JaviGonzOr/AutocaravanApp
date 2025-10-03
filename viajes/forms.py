from django import forms
from .models import Viaje, Archivo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'origen', 'destino']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'origen': forms.TextInput(attrs={'id': 'origen', 'placeholder': 'Ciudad de salida'}),
            'destino': forms.TextInput(attrs={'id': 'destino', 'placeholder': 'Ciudad de destino'}),
        
        }

# Form para un solo archivo
class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo']
        
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

