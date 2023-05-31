from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from datetime import datetime

def add_todo(request):
    if request.method == 'POST':  # Corrected capitalization of 'POST'
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_todos')
    else:
        form = TodoForm()
    return render(request, 'todo.html', {'form': form})


def display_todos(request):
    todos = Todo.objects.all()
    return render(request, 'display_todos.html', {'todos': todos})

def display_by_category(request,category):
    todos=Todo.objects.filter(category__name=category)
    context={
        'category':category,
        'todos':todos
    }
    return render(request,'category.html',context)


def mark_todo_done(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.has_been_done = True
    todo.date_completion = datetime.now()
    todo.save()
    return redirect('display_todos')

def mark_todo_undone(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.has_been_done = False
    todo.date_completion = None
    todo.save()
    return redirect('display_todos')


