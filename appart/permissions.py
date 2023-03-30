from rest_framework.permissions import BasePermission


class CanEditOwnedApartment(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class CanDeleteOwnedApartment(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
