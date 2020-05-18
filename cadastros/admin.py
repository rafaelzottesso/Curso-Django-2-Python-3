from django.contrib import admin

# Importar as classes
from .models import Campus, Servidor, Status, Situacao, Classe, Progressao, Campo, Atividade, Comprovante, Validacao

# Register your models here.
admin.site.register(Campus)
admin.site.register(Servidor)
admin.site.register(Status)
admin.site.register(Situacao)
admin.site.register(Classe)
admin.site.register(Progressao)
admin.site.register(Campo)
admin.site.register(Atividade)
admin.site.register(Comprovante)
admin.site.register(Validacao)
