from rest_framework import permissions

class IsAdminReadAndWriteOnly(permissions.BasePermission):
    """
    Custom permission to only allow Admin access to data.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to Admins only
        user = request.user
        return 'Admin' in user.role

class IsAdminOrOwnsAccount(permissions.BasePermission):
    """
    Custom permission to only allow Admins and account owners only
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to Admins and account owners only
        user = request.user
        return 'Admin' in user.role or (str(user.id) == str(obj['id']))
