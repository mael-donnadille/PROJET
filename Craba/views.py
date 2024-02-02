from django.http import HttpResponse
from django.shortcuts import render
#from .models import Lieu
def home(request):
   return render(request, 'accueil.html')


def page_entre(request):
   return render(request, 'enterprise.html')

def page_carte(request):
   return render(request, 'carte.html')




