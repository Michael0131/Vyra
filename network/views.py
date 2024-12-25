from django.shortcuts import render
from django.http import HttpResponse  # To send a basic HTTP response
# Create your views here.

def test_view(request):
    return HttpResponse("Hello this is the network app test view") # This is a placeholder view that sends a simple response to test routing