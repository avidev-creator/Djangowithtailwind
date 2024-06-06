from django.shortcuts import render,HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    responde_data = render_to_string("api/api.html")
    return HttpResponse(responde_data)