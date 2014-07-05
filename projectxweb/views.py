from django.http import HttpResponse
from models import *

def home(request):
    user = User(acces_token = "abcdefghijklmnopqrstuvwxyz", source = 1, name = "Sreenivas Kodur")
    user.save()
    return HttpResponse("Welcome to Projectx server! \n Just added an entry to DB")
