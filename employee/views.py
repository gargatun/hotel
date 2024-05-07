from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from employee.forms import LoginUserForm
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'employee/login.html'
    redirect_authenticated_user = False  # Allow authenticated users to see the login page
    success_url = reverse_lazy('employee:index')

    def get(self, request, *args, **kwargs):
        # No custom redirection logic, just call the superclass method
        return super().get(request, *args, **kwargs)
    
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'employee/index.html'
    login_url = '/employee/login/'  # Explicitly specify where to redirect unauthenticated users
    redirect_field_name = 'next'  # This will append '?next=/employee/' to the login URL

