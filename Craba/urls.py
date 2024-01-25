from django.urls import path

from Craba import views
from Craba.views import home

urlpatterns = [
    path('', views.home),
]