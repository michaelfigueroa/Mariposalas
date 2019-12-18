from django.shortcuts import render
from .models import PanPascua

def index(request):
    return render(request,"pandepascua/index.html")

def res(request):
     Datos=PanPascua.objects.all()
     return render(request, "pandepascua/resultado.html",{"pandepascua":Datos})
