from django.urls import path
from mysite_app import views

urlpatterns = [
    path('', views.home, name='home'),
]