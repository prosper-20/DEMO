from django.urls import path
from .views import HomeView, TaskDetailView, TaskUpdateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("detail/<slug>", TaskDetailView.as_view(), name="detail"),
    path("update/<slug>/", TaskUpdateView.as_view(), name="update"),
]