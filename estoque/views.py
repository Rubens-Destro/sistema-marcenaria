from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Produto 


def listar_produtos(request):
    produtos = list(Produto.objects.values())
    return JsonResponse(produtos, safe=False)

@csrf_exempt
def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco', 12)

        produto = Produto.objects.create(
            nome=nome,
            descricao=descricao,
            quantidade=quantidade,
            preco=preco,
        )

        return JsonResponse({
            "produto": model_to_dict(produto),
            "mensagem": "Produto criado com sucesso",
        })
    
    return JsonResponse({
            "erro": "metodo não permitido"
        }, status=405)


