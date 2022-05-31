from django.contrib import admin
from .models import Comentario, User, Lance, Produto


# Register your models here.

admin.site.register(User)
admin.site.register(Produto)
admin.site.register(Lance)
admin.site.register(Comentario)




