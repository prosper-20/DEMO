from django.urls import path
from .views import HomeView, TaskDetailView, TaskUpdateView, TaskCreateView, UserHomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("detail/<slug>", TaskDetailView.as_view(), name="detail"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("update/<slug>/", TaskUpdateView.as_view(), name="update"),
    path("user/<str:user>/", UserHomeView, name="user_home")
]