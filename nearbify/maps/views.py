from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_client_id = '873fbe1552b44761a4635e9c16250e6d'     # Your client id
    my_secret = 'bf78ff34e9cb4d519197aabd77999092'    # Your secret
    redirect_uri = 'http://localhost:8888/callback'  # Your redirect uri
    return HttpResponse("Hello, nearbify")

def spotify_callback(request):
    return HttpResponse("spotify callback")
