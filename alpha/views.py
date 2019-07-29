from django.shortcuts import render
from django.template import RequestContext
from .models import Location, Timeshot, Details, Image

# Create your views here.
def index(request):
    title = "Ramza Ombati"
    return render(request, 'index.html', {"title": title})

def photos(request):
    title = "Ramza | Photography"

    image = []
    for image in image:
        image.append(image)
    return render(request, 'photos.html', {"title": title, "image": image})

def email(request):
    return render(request, 'email.html')
    
