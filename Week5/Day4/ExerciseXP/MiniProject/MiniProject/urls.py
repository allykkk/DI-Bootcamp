"""
URL configuration for MiniProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import add_todo, display_todos, display_by_category, mark_todo_done, mark_todo_undone

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', add_todo, name="add_todo"),
    path('todos/', display_todos, name="display_todos"),
    path('todos/<str:category>/', display_by_category, name='display_by_category'),
    path('todo_done/<int:todo_id>/', mark_todo_done, name='mark_todo_done'),
    path('todo_undone/<int:todo_id>/', mark_todo_undone, name='mark_todo_undone'),
]
