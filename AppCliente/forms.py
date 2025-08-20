from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCliente.models import mensajes, usuario

class ContactoForm(forms.ModelForm):
    class Meta:
        model = mensajes
        fields = ['nombre', 'email', 'mensaje', 'fecha']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'rows': 2, 'cols': 50, 'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }

class RegistroUsuarioForm(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=50)
    ciudad = forms.CharField(max_length=50)
    codigo_postal = forms.CharField(max_length=50)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido', 'email',
                  'telefono', 'direccion', 'ciudad', 'codigo_postal', 'fecha_nacimiento']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}