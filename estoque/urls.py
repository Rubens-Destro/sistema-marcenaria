from django.urls import path
from .views import listar_produtos

urlpatterns = [
    path('produtos/', listar_produtos),
]
