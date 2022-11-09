from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'

class DetalheProduto(View):
    def get(self , *args , **Kwargs):
        return HttpResponse('DetalheProduto')


class AdicionarAoCarrinho(View):
    def get(self , *args , **Kwargs):
        return HttpResponse('AdicionarCarrinho')


class RemoverDoCarrinho(View):
    def get(self , *args , **Kwargs):
        return HttpResponse('RemoverCarrinho')


class Carrinho(View):
    def get(self , *args , **Kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self , *args , **Kwargs):
        return HttpResponse('Finalizar')


