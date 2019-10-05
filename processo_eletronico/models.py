from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    endereco = models.CharField(max_length=11, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.IntegerField(null=True)
    carga_horaria = models.IntegerField(null=True)
    salario = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    quantidade_funcionario = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Processo(models.Model):
    numero = models.IntegerField(null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Pessoa, related_name='pessoas', null=True, blank=True, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento,related_name='Departamentos', null=True, blank=True, on_delete=models.SET_NULL)
    interessada = models.ManyToManyField(Pessoa, related_name='Interessadas')
    Investigada = models.ManyToManyField(Pessoa, related_name='Investigadas')

    def __str__(self):
        return self.usuario.nome

class Tramitacoes(models.Model):
    processo = models.ForeignKey(Processo, related_name='processo', null=True, blank=True, on_delete=models.PROTECT)
    origem = models.ForeignKey(Departamento, related_name='origem', null=True, blank=True, on_delete=models.PROTECT)
    destino = models.ForeignKey(Departamento, related_name='destino', null=True, blank=True, on_delete=models.PROTECT)
    data_movimentacao = models.DateField()

    def __str__(self):
        return self.origem.nome

class Documento(models.Model):
    processo = models.ManyToManyField(Processo)
    titulo = models.CharField(max_length=50)
    data = models.DateField()
    texto = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo

class PortariaDeInstauracao(Documento):
    inicio_do_processo = models.DateTimeField(auto_now_add=True)
    minuta = models.CharField(max_length=50)

    def __str__(self):
        return self.minuta

class PedidoDePrazo(Documento):
    justificativa = models.CharField(max_length=50)
    prazo_anterior = models.DateField()
    novo_prazo = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.justificativa

class EnvioDeProcesso(Documento):
    justificativa = models.CharField(max_length=50)
    prazo_anterior = models.DateField()
    novo_prazo = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.justificativa



