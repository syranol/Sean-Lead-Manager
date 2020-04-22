from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # make sure frontend load before leads
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
    path('', include('accounts.urls'))
]
