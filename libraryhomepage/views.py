from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def get_homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def get_bookpage(request):
    template = loader.get_template('livro.html')
    return HttpResponse(template.render())