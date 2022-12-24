from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Разрешения для действий с пользователями от имени администратора"""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
            or request.user.is_staff
            or request.user.is_superuser
        )
