from django.contrib import admin
from django.urls import path, include
from .views import listar_postagem, adicionar_postagem, alterar_postagem, excluir_postagem, postagem_especifica

urlpatterns = [
    path('', listar_postagem),
    path('add/', adicionar_postagem),
    path('alter/<id>', alterar_postagem),
    path('delete/<id>', excluir_postagem),
    path('postagem/<id>',postagem_especifica),
    
]