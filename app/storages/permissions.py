from rest_framework import permissions


class IsCompanyMember(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if view.action == 'create':
            return hasattr(request.user, 'owned_company')

        return True


    def has_object_permission(self, request, view, obj):
        return request.user.company == obj.company