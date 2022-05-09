from django.shortcuts import render
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import views, status
from rest_framework.response import Response
from geek.settings import EMAIL_HOST_USER
class geek(View):
    def send_mail1(self):
            first_name="Ankit"
            last_name="Tiwari"
            email='shristi.katiyar@tothenew.com'
            subject = 'welcome to Ankit Tiwari E-commerce Websites'
            message = f'Hi {first_name} {last_name}, Your order has been done'
            email_from = EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            # response={'data':'message'}
            # return Response(response, status=status.HTTP_200_OK)
            return HttpResponse('hello world')