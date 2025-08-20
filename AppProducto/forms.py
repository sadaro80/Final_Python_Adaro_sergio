from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cod', 'categoria', 'nombre', 'precio', 'descripcion', 'stock', 'imagen']
        widgets = {
            'cod': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cod', 'categoria', 'nombre', 'precio', 'descripcion', 'stock']

