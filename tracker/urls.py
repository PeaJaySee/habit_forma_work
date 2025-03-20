from . import views
from django.urls import path


urlpatterns = [
    path('', views.HabitListView.as_view(), name='home'),
    
]