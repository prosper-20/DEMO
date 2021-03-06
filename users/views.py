from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, your account has been created successfully!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)