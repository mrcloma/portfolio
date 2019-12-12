from django.db import models


class Contatos(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    telefone_fixo = models.IntegerField(
        null=False,
        blank=False
    )

    telefone_celular = models.IntegerField(
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    descricao = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    objetos = models.Manager()
