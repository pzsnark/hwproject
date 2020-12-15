from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse("Корневое приложение")

def index(request):
    html = "<html><body><a href='http://localhost:8000/bb/'>Доска объявлений<a/><br>" \
           "<a href='http://localhost:8000/bb/current_time'>Текущее время<a/></body></html>"
    return HttpResponse(html)

