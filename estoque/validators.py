from django.core.exceptions import ValidationError

def validar_quantidade_nao_negativa(value):
    if value < 0:
        raise ValidationError("O valor informado é menor que zero")