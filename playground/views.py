from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> Response
# Request handler
# action (Rails) -> view (Django)

def say_hello(request):
    return HttpResponse('Hello World')
    
