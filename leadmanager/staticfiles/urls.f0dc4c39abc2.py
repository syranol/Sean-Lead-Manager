#So we can describe a path for our url
from django.urls import path
from . import views

urlpatterns = [
    #for root directory, load
    path('', views.index)
]
