from django.urls import path, include


urlpatterns: list[path] = [
    path('todo/', include('todo.api.urls'), name='todo-api')
]

