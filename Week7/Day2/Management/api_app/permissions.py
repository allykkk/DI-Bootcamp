from rest_framework.permissions import BasePermission

class IsDepartmentAdmin(BasePermission):
    def has_permission(self, request,view):
        user=request.user
        return getattr(user, 'is_department_admin', False)