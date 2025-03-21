from . import views
from django.urls import path



urlpatterns = [
    path('', views.HabitListView.as_view(), name='home'),
    path('habit/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit_update'),
]