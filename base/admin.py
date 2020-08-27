from django.contrib import admin
from .models import BaseUser, Categoria, Movimento


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo', 'categoria')


@admin.register(Movimento)
class MovimentoAdmin(admin.ModelAdmin):
    list_display = ('user', 'data', 'categoria', 'descricao', 'valor')



