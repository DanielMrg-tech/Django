from django.urls import path
from books import views


urlpatterns = [
    path('hello', views.hello, name='hello')
]