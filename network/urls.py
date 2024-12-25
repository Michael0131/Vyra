from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls), # Default admin interface
    path('network/', include ('network.urls')),   # Any URL starting with 'network/' will be handled by the urls.py in the 'network' app
    path('test/', views.test_view, name ="test") # Maps the URL 'network/test/' to the 'test_view' function in views.py
]