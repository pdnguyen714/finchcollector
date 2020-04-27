from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return HttpResponse ('<h1>About the Finch Collector<h1>')