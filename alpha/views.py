from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def index(request):
    title = "Ramza Ombati"
    return render(request, 'index.html', {"title": title})

def photos(request):
    title = "Ramza | Photography"
    return render(request, 'photos.html', {"title": title})