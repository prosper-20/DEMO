from distutils.log import Log
from re import template
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# def UserHomeView(self, request, **kwargs):
#     user = self.request.user
#     task = Task.objects.filter(user=user)
#     username=self.kwargs.get("username")
#     context = {
#         "task": task,
#         "username": username,
#     }
#     return render(request, "main/user_tasks.html", context)


class UserHomeView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Task
    template_name = "main/user_tasks.html"
    context_object_name = "tasks"


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Task.objects.filter(user=user)

    def test_func(self):
        task = self.get_object()
        if task.user == self.request.user:
            return True
        return False


def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # This returns the results of the user's search
        tasks = Task.objects.filter(title__contains=searched)
        return render(request, "main/new_search_posts.html", {'searched': searched, 'tasks': tasks})
    else:
        return render(request, "main/new_search_posts.html")

class HomeView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "main/task_list_1.html"

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "completed", "slug"]
    template_name = "main/task_form_1.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ["title", "description", "completed", "slug"]
    template_name = "main/task_form_1.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        if task.user == self.request.user:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if task.user == self.request.user:
            return True
        return False






    
        





