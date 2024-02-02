from django.urls import path

from Craba import views
from .views import page_entre, page_carte


urlpatterns = [
    path('', views.home),
    path('entreprise/', page_entre, name='entreprise'),
    path('carte/', page_carte, name='carte'),


]
