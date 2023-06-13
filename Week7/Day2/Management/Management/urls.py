"""
URL configuration for Management project.

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
from api_app.views import (
    DepartmentListAPIView,
    DepartmentCreateAPIView,
    DepartmentDetailAPIView,
    EmployeeListAPIView,
    EmployeeCreateAPIView,
    EmployeeDetailAPIView,
    ProjectListAPIView,
    ProjectRetrieveAPIView,
    ProjectUpdateAPIView,
    ProjectDestroyAPIView,
    TaskListAPIView,
    TaskRetrieveAPIView,
    TaskUpdateAPIView,
    TaskDestroyAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('departments/create/', DepartmentCreateAPIView.as_view(), name='department-create'),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectRetrieveAPIView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectUpdateAPIView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDestroyAPIView.as_view(), name='project-delete'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDestroyAPIView.as_view(), name='task-delete'),
]
