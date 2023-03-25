from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Vista de APP")
def sumar(request, x,y):
    sum=x+y
    return HttpResponse("La suma de {x} + {y} es igual a {sum}".format(x=x,y=y,sum=sum))
def restar(request, x,y):
    res=x-y
    return HttpResponse("La resta de {x} - {y} es igual a {res}".format(x=x,y=y,res=res))
def multiplicar(request, x,y):
    mult=x*y
    return HttpResponse("La multiplicacion de {x} x {y} es igual a {mult}".format(x=x,y=y,mult=mult))