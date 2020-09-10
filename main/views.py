from django.shortcuts import render
from .models import Prispevok
def forum(request):
    return render(request,('main/forum.html'),{'prispevky':Prispevok.objects.all()})
