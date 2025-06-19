from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")  # Or use LoginRequiredMixin
        if request.user.user_type.user_type_name != "Admin":
            raise PermissionDenied("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)
