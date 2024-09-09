from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'customer') and request.user.customer.is_owner == True