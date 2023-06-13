from rest_framework import serializers
from .models import Department, Employee, Project, Task


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_project(self, obj):
        return obj.project.name
