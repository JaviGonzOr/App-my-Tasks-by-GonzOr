from django.contrib import admin
from .models import Tarea, ImagenTarea, Proveedor, Producto
from .forms import ProductoForm, TareaForm, ProductoForm, ProveedorForm



class ImagenTareaAdmin (admin.TabularInline):
    model = ImagenTarea

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['proveedor']
    search_fields = ['proveedor']
    list_filter = ['proveedor']
       
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'proveedor']
    search_fields = ['modelo']
    list_filter = ['modelo', 'proveedor']


class TareaAdmin (admin.ModelAdmin):
    list_display = ['cliente', 'titulo', 'usuario', 'completado', 'creacion']
    search_fields = ['titulo', 'cliente']
    list_filter = ['titulo', 'completado', 'cliente']
    inlines = [
        ImagenTareaAdmin
    ]






admin.site.register(Tarea, TareaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)





