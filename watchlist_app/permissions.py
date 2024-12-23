from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.user.is_staff:
			return True
		return request.user.is_authenticated and request.method in permissions.SAFE_METHODS
