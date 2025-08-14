from django.db import models
from .validators import validar_quantidade_nao_negativa 

class Produto(models.Model):
    nome = models.CharField(max_length=1000)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(
        validators=[validar_quantidade_nao_negativa]
    )
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    def __str__(self):
        return self.nome