from django import forms 
from .models import Tarea, Producto, Proveedor


class TareaForm (forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'cliente', 'proveedor', 'modelo', 'descripcion', 'material', 'importante'] 
        widjets = {
            'titulo': forms.TextInput (attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput (attrs={'class': 'form-control'}),
            'material': forms.Textarea (attrs={'class': 'form-control'}),
            'importante': forms.CheckboxInput (attrs={'class': 'form-check-input'})
        }

class ProveedorForm (forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['proveedor']

class ProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['modelo', 'ficha_tecnica']


from django import forms

class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True)
    
    email=forms.CharField(label="Email", required=True)

    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)








