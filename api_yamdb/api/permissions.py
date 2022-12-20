from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Разрешения для действий с пользователями от имени администратора"""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'admin' # админ
            or request.user.is_staff
            or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return request.method in ('GET', 'POST', 'PATCH', 'DELETE')


class MePermission(permissions.BasePermission):
    """Разрешения для действий с пользователями для пользователей"""
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, view, request, obj):
        return request.method in ('PATCH', 'GET')


class IsAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and (
                request.user.role == 'admin' or request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and (
                request.user.role == 'admin' or request.user.is_superuser)
        )


class IsAdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == 'ADMIN'
                or request.user.role == 'MODERATOR'
                or obj.author == request.user)
