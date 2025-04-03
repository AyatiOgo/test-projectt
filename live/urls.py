from .views import *
from django.urls import path


urlpatterns = [
    path('', homeview, name='home'),

] 