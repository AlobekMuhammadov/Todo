from django.shortcuts import render, redirect
from .models import *

def rejalar(request):
    if request.method == 'GET':
        content = {
            'rejalar':Reja.objects.all()
    }
        return render(request,'todo.html',content)

    elif request.method == 'POST':
        Reja.objects.create(
            sarlavha = request.POST.get('s'),
            batafsil = request.POST.get('b'),
            yonalish = Reja.objects.get(yonalish=request.POST.get('y')),
        )
        return redirect('')


def reja_ochir(request,son):
    Reja.objects.filter(id=son).delete()
    return redirect('')




