from django.shortcuts import render, get_object_or_404
import requests 
from django.http import JsonResponse
from .models import Postagem

# Create your views here.


def listar_postagem(request):
    
    postagens = Postagem.objects.all()
    return JsonResponse(postagens)

def adicionar_postagem(request):
    if request.method == 'POST':
        valores = request.content_params
        Postagem.objects.create(valores)
        return JsonResponse({'message': 'sucesso',
        'status_code':200})

        pass

def alterar_postagem(request, id_post):
    if request.method == 'PUT':
        try:
            objeto = Postagem.objects.filter(id=id_post).update()
            return JsonResponse({'message': 'sucesso',
            'code':200})
        except:
            return JsonResponse({'message': 'erro',
            'status_code':404})


def excluir_postagem(request, id_post):
      if request.method == 'DELETE':
        objeto = Postagem.objects.filter(id=id_post).delete()

        return JsonResponse({'message': 'sucesso',
        'status_code':200})

def postagem_especifica(request, id):
    
    postagens = Postagem.objects(id)
    return JsonResponse(postagens)





