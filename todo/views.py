from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from .forms import TodoForm
from todo.models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    todo_form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'todos.html', context={'todos': todos, 'todo_form': todo_form})


def done_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.is_Complete = not todo.is_Complete
        todo.save()
    return HttpResponseRedirect('/')


def remove_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
    return HttpResponseRedirect('/')


def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo_form = TodoForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save(commit=False)
            todo.title = todo_form.cleaned_data['title']
            todo.save()
    return HttpResponseRedirect('/')
