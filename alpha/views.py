from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def index(request):
    title = "Ramza  | Home"
    return render(request, 'index.html', {"title": title})
