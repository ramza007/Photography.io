import markdown
from pathlib import Path

from django.shortcuts import render
from django.template import RequestContext
from .models import Location, Timeshot, Details, Portraits, NewsletterRecepients, Landscape, Architecture, Automobiles
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .email import send_welcome_email
from django.conf import settings
from django.utils.html import escape



# Create your views here.
def index(request):
    title = "Ramsa Ombati"
    return render(request, 'index.html', {"title": title})

def photos(request):
    title = "Ramsa | Portaits"
    content = Portraits.objects.all()
    return render(request, 'photos.html', {"title": title, "content": content})

def email(request):
    title = "Ramsa | Email"
    form = NewsLetterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsletterRecepients(name=name, email=email)
            recipient.save()
            # send_welcome_email(name, email)

            return HttpResponseRedirect('thank-you')

    return render(request, 'email.html', {"title": title, "letterForm":form})

def thankyou(request):
    title = "Ramsa | Thank You"
    name = email(request)
    return render(request, 'thank-you.html', {"title": title})


def landscapes(request):
    title = "Photocase | Landscapes"
    landscapes_content = Landscape.objects.all()
    return render(request, 'photocase/landscapes.html', {"title": title, "landscapes_content": landscapes_content})

def architecture(request):
    title = "Photocase | Architecture"
    architecture_content = Architecture.objects.all()
    return render (request, 'architecture.html', {"title": title, "architecture_content": architecture_content})


def automobiles(request):
    title = "Photocase | Automobiles"
    automobiles_content = Automobiles.objects.all()
    return render (request, 'automobiles.html', {"title": title, "automobiles_content": automobiles_content})

def resume(request):
    title = "Ramsa Ombati - Resume"
    
    # Construct the path to the Markdown file
    markdown_file_path = "./README.md"
    
    # Read the Markdown file
    with open(markdown_file_path, 'r') as file:
        markdown_content = file.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    
    # Create context
    context = {
        "title": title,
        "markdown_content": html_content
    }
    
    return render(request, 'resume.html', context)

# Error pages

def error_404(request, exception):
    return render(request, 'error_404.html', status=404)


def error_500(request):
    return render(request, 'error_500.html')
