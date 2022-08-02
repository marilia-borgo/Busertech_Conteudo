from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Postagem (models.Model):
    url = models.URLField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data= models.DateField(default=timezone.now)
    descricao = models.TextField(max_length=200)
    
