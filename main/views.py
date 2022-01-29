import imp
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Task

class HomeView(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetailView(DetailView):
    model = Task
    context_object_name = "tasks"





