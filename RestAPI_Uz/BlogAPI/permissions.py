from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #faqat kurish boshqalarga
        if request.method in permissions.SAFE_METHODS:
            return True
        #post faqat adminga
        return obj.author == request.user