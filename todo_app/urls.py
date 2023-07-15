from django.urls import path
from .views import ListTodoView, DetailTodoView

urlpatterns = [
    path('todo/', ListTodoView.as_view()),
    path('todo/<pk>/', DetailTodoView.as_view())
]