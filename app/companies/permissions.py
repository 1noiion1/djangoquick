from rest_framework import permissions

class IsCompanyOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

    def has_permission(self, request, view):
        if view.action == 'create':
            return not hasattr(request.user, 'owned_company')
        return True