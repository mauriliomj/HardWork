from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

class Pagar(View):
    def get(self, *args, **Kwargs):
        return HttpResponse('Pagar')

class FecharPedido(View):
    def get(self , *args , **Kwargs):
        return HttpResponse('FecharPedido')


class Detalhe(View):
    def get(self , *args , **Kwargs):
        return HttpResponse('Detalhe')
