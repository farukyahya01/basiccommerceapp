from rest_framework import permissions


# THE USER ONLY CAN DO OWN PROCESS
#   

class IsProfileRecordOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user == obj.user
        return request.user == obj.user
        