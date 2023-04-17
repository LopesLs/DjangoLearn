# All urls for the library homepage app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_homepage, name='homepage'),
    path('books/', views.get_bookpage, name='bookpage'),
]