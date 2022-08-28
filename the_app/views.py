from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    the_response_string = 'Goodbuy, World! Enjoy the sale!'
    return HttpResponse(the_response_string)

