from django.urls import path, re_path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("product", views.product, name="product"),
    path("<int:Produto_id>", views.titulo2, name="titulo2"),
    path("<int:prinfo_id>/n", views.n, name="n"),
    path("<int:prinfo_id>/encerrar", views.encerrar, name="encerrar"),
    path("<int:prinfo_id>/comentario", views.comentario, name="comentario"),
    path("<int:prinfo_id>/favorits", views.favorits, name="favorits"),

    path("f", views.f, name="f")


]
