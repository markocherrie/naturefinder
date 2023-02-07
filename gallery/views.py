from django.http import HttpResponse
from django.template import loader
from .models import IMG
from django.shortcuts import render

# Create your views here.
def gallery(request):
    data = IMG.objects.all()
    context = {
        'data' : data
    }
    return render(request,"gallery.html", context)