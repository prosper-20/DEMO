import imp
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
)
from .models import Task

class HomeView(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"

class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
        





