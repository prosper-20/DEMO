from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, "Hi {username}, your account has been created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)