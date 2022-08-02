from multiprocessing import context
from turtle import pos
from django.shortcuts import render, get_object_or_404
import requests
import  json
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import Postagem
from django.forms.models import model_to_dict

# Create your views here.


def listar_postagem(request):
    
    # postagens = list(Postagem.objects.all().values_list('id', 'autor__username'))
    postagens = Postagem.objects.all().select_related('autor')
    c = []
    for postagem in postagens:
        c.append({
            'id': postagem.id,
            'autor': postagem.autor.username,
            'url': postagem.url,
            'descricao': postagem.url
        })
    context = {'postagens': c}
    return JsonResponse(context)
@csrf_exempt
def adicionar_postagem(request):
    if request.method == 'POST':
        valores = request.body
        post = json.loads(valores.decode('utf-8'))
        Postagem.objects.create(autor_id=1, descricao=post.get('descricao'), url=post.get('url'))
        return JsonResponse({'message': 'sucesso',
                             'code': 200})


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





