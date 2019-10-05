from django.contrib import admin
from .models import Pessoa, Funcionario, Departamento, Processo, Tramitacoes, Documento, PortariaDeInstauracao, PedidoDePrazo, EnvioDeProcesso

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Processo)
admin.site.register(Tramitacoes)
admin.site.register(Documento)
admin.site.register(PortariaDeInstauracao)
admin.site.register(PedidoDePrazo)
admin.site.register(EnvioDeProcesso)