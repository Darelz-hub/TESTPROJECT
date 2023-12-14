from django.contrib import admin
from django.urls import path, include
import test.views as test
urlpatterns = [
    path('tests/', test.informations)
]