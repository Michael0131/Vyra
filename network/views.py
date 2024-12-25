from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()  # Show an empty form for GET requests
    return render(request, 'registration/signup.html', {'form': form})
