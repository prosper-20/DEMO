from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def UserHomeView(self, request):
    user = self.request.user
    task = Task.objects.filter(user=user)
    context = {
        "task": task
    }
    return render(request, "main/user_tasks.html", context)


class HomeView(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = "__all__"


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
        if task.author == self.request.user:
            return True
        return False



    
        





