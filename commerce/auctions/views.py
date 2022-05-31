#from crypt import methods
from inspect import FullArgSpec
from urllib import request
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models.query_utils import DeferredAttribute

from .models import User, Produto, Lance, Comentario


def index(request):
    produto1 = Produto.objects.all()
    comentario = Comentario.objects.all()
    return render(request, "auctions/index.html",{
        "Produto": produto1,
        "comentario": comentario
        
    })
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def product(request):
    return render(request, "auctions/product.html")




def f(request):
    print("x")
    if request.method == "POST":
        titulo = request.POST['titulo']
        user = request.user 
        descricao = request.POST['descricao']
        categoria = request.POST['categoria']
        img = request.POST['img']
        lance1=request.POST['lance1']
        #lance = Lance(lance=int(request.POST['lance'], user))
        
        s_lance = Produto(titulo = titulo, user = user, descricao = descricao , categoria = categoria, img = img, lance1 = lance1)
        s_lance.save()
        print(s_lance)
        return render(request, "auctions/index.html", {
            "a": s_lance.titulo,
            "b": user,
            "c": descricao,
            "d": categoria,
            "f": img,
            "l": lance1

        })

    else:
        return render(request, "auctions/login.html")

    
def titulo2(request, Produto_id):
    prinfo = Produto.objects.get(pk=Produto_id)
    comentario1 = Comentario.objects.all()
    if request.user == Produto.user:
        dono = True
    else:
        dono = False
        
    return render(request, "auctions/titulo2.html",{
        "prinfo": prinfo,
        "dono": dono,
        "comentario": comentario1
        })

def n(request, prinfo_id):
    prinfo = Produto.objects.get(pk=prinfo_id)

    nova_aposta = int(request.POST['numb'])
    aposta_i = int(prinfo.lance1)
    print(request.POST['numb'])
    print(aposta_i)

    mensagem = str("You bet didn't match!")
    mensagem_menor = str("Your bet was aproved")

    if aposta_i > nova_aposta:
        return render(request, "auctions/titulo2.html",{
            "nova_aposta": nova_aposta,
            "prinfo": prinfo,
            "mensagem": mensagem
        })  

    else:
        novo_lance = Lance(lance = int(nova_aposta), usr=request.user)
        novo_lance.save()
        prinfo.lance1 = int(nova_aposta)
        prinfo.save()
        return render(request, "auctions/titulo2.html",{
            "nova_aposta": nova_aposta,
            "prinfo": prinfo,
            "mensagem": mensagem_menor,
            "novo_lance": novo_lance,

        })

def encerrar(request, prinfo_id):
    prinfo = Produto.objects.get(pk=prinfo_id)
    prinfo.encerrar = True
    prinfo.save()
    return HttpResponseRedirect(reverse("titulo2", args=(prinfo_id,)))

def comentario(request, prinfo_id):
    if request.method == "POST":
        autor = request.user 
        comentario_v = request.POST["comentario"]
       # produto1 = Produto.objects.get(pk=prinfo_id)
      #  produtoc = Comentario.produto1
        print(comentario_v)
        print(autor)
        comentario_novo = Comentario(text = comentario_v, escritor = autor)
        comentario_novo.save()
       # print(produto1)
      #  print(comentario.produto1)
    return HttpResponseRedirect(reverse("titulo2", args=(prinfo_id,)))


def favorits(request,prinfo_id):
    user = request.user
    prinfo = Produto.objects.get(pk=prinfo_id)
    prinfo.favorits.add(user)
    return HttpResponseRedirect(reverse("titulo2",args=(prinfo_id,)))