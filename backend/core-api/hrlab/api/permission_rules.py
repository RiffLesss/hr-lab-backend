from rest_framework import permissions

# we'll need it later

# class IsAdminPermission(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         return super().has_permission(request, view) and request.user.is_admin
#
#
# class HasMethodPermission(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         # basemane в urls
#         method_permission_to_check = view.basename + "_" + view.action
#         return super().has_permission(request, view) and request.user.has_method_permission(method_permission_to_check)
