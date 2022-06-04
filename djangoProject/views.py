from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.core.mail import send_mail

from django.core.mail import send_mail


def home_view(request) :
    return render(request, 'home.html')


def place_your_order_view(request):

        if request.method == "POST":
            subject = 'Friends Factory'
            email = request.POST.get('email')
            username = request.POST.get('Name')
            Message = request.POST.get('Message')
            email_message = str(email) + '\n' + str(username) + '\n' + str(Message)
            mail = EmailMessage(subject, email_message, to=['friendsplastic18@gmail.com'])
            mail.send()
        return render(request, 'placeyourorder.html')
        return render(request, 'home.html')

