from django.contrib import admin
from blog.models import autor
from blog.models import articulo
from blog.models import seccion

# Register your models here.
admin.site.register(articulo)
admin.site.register(autor)
admin.site.register(seccion)
