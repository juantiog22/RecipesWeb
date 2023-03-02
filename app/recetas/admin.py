from django.contrib import admin
from .models import Receta

# Register your models here.


class RecetaAdmin(admin.ModelAdmin):

    list_display = ('name', 'created')



admin.site.register(Receta)