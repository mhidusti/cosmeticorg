from django.shortcuts import redirect
from .forms import CustomUserCreation
from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticationForm
from django.views.generic import FormView, CreateView, TemplateView


class LoginView(FormView):
     template_name = 'registration/login.html'
     form_class = AuthenticationForm
     success_url = '/'
     def form_valid(self, form):
         email = self.request.POST.get('email')
         password = self.request.POST.get('password')
         user = authenticate(email=email, password=password)
         if user is not None:
              login(self.request, user)
              return super().form_valid(form)
         


class LogOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')



class SignUpView(CreateView):
     template_name = 'registration/signup.html'
     form_class = CustomUserCreation
     success_url = '/accounts/login/'
