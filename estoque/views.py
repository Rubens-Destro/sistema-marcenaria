from django.http import JsonResponse
from .models import Produto 

def listar_produtos(request):
    produtos = list(Produto.objects.values())
    return JsonResponse(produtos, safe=False);