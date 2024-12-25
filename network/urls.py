from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('signup/', views.signup, name='signup'),  # Add this line
]