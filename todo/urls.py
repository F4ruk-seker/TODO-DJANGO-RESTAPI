from django.contrib import admin
from django.urls import path
from .views import todo_list, done_todo,remove_todo,update_todo


urlpatterns = [
    path('', todo_list),
    path('done/<todo_id>', done_todo),
    path('remove/<todo_id>', remove_todo),
    path('update/<todo_id>', update_todo),
]


