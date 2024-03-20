from django.urls import path
from . import views


app_name = 'todo-api'

urlpatterns: list[path] = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', views.TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo')
]

