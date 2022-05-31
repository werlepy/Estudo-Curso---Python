#from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
#from tkinter import CASCADE
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class  Lance(models.Model):
    lance = models.IntegerField(default=0)
    usr = models.ForeignKey(User, on_delete = models.CASCADE, related_name= "teste")

    def __str__ (self):
        return f"Bid of {self.lance} from {self.usr}"

class Produto(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Produto", default=None)
    img = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=50)
    lance1 = models.IntegerField(default=0)
    encerrar = models.BooleanField(default=False, blank=True, null=True)
    favorits = models.ManyToManyField(User, blank=True, related_name="favorits")
    #bid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Lance", default=None)


    def __str__(self):
        return f"{self.titulo}: {self.descricao} {self.user}"

class Comentario(models.Model):
    text = models.CharField(max_length=400)
    escritor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "comentario")
    #produto1 = models.ForeignKey(Produto, on_delete = models.CASCADE, related_name = "comentario")

    def __str__(self):
        return f"Comentário: {self.text} writen by:{self.escritor}"


