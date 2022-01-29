from django.urls import path
from .views import HomeView, TaskDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("detail/<slug>", TaskDetailView.as_view(), name="detail"),
]