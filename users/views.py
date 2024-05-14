from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, TemplateView

class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Register Successfully. Please Login.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Something is wrong, Please try again.')
        return super().form_invalid(form)
    

class UserLoginView(LoginView):
    template_name = 'form.html'
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
class UserProfileView(TemplateView):
    template_name = 'users/profile.html'