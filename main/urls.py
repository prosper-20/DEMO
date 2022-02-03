from django.urls import path
from .views import HomeView, TaskDetailView, TaskUpdateView, TaskCreateView, search_posts, TaskDeleteView
from . import views
# UserHomeView,


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("detail/<slug>", TaskDetailView.as_view(), name="detail"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("update/<slug>/", TaskUpdateView.as_view(), name="update"),
    path('delete/<slug>/', TaskDeleteView.as_view(), name="delete"),
    # path("user/<str:username>/", UserHomeView.as_view(), name="user_home"),
    path("search_posts/", views.search_posts, name='search_posts'),
]