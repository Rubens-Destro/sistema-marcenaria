from django.urls import path
from .views import listar_produtos, criar_produto


urlpatterns = [
    path('produtos/', listar_produtos),
    path('produtos/adicionar/', criar_produto),
]
