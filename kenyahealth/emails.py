from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
#define your email methods here
def send_welcome_email(username,receiver):
    subject = 'Welcome to the eafya application'
    sender = 'langatfarmer@gmail.com'
    #passing in the context variables
    text_content = render_to_string('email/wel.txt',{"username":username})
    html_content = render_to_string('email/wel.html',{"username":username})

    msg =  EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
