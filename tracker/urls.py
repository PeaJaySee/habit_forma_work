from . import views
from django.urls import path

urlpatterns = [
    path("", views.HabitList.as_view(), name="home"), #placeholder
]