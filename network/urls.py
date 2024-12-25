from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('test/', views.test_view, name="test"),  # Map 'test/' to test_view in views.py
]