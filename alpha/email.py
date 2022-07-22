from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):

    #this is the message
    subject = " Welcome To Ramsa's Universe !! "
    sender = 'Ramsa Ombati'

    #contex variables
    text_content = render_to_string('email/newemail.txt', {"name": name})
    html_content = render_to_string('email/newemail.html', {"name": name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()