from django.contrib import admin
from django.urls import path, include
from .views import main_page


app_name = 'mainpage'

urlpatterns = [
    path('', main_page, name='mainpage_view'),
]