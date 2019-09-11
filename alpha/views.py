from django.shortcuts import render
from django.template import RequestContext
from .models import Location, Timeshot, Details, Image, NewsletterRecepients
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .email import send_welcome_email

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
    title = "Ramza | Email"
    form = NewsLetterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsletterRecepients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            return HttpResponseRedirect('/')

    return render(request, 'email.html', {"title": title, "letterForm":form})
