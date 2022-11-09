from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class ListaProdutos(ListView):
    pass

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


