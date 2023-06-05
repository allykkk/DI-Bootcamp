from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .forms import SignupForm, LoginForm

class SignupView(View):
    def get(self,request):
        form=SignupForm()
        return render(request,'accounts/signup.html',{'form':form})

    def post(self,request):
        form=SignupForm(request.POST)
        if form.is_valid():
            user =form.save()
            # password1 is the user typed password, password2 is password confirmation
            auth_user = authenticate(
                request, username=user.username, password=request.POST['password1']
            )
            if auth_user is not None:
                auth_login(request, auth_user)
                return redirect('films:homepage')
        return render(request, 'accounts/signup.html', {'form': form})



class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self,request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('films:homepage')
        return render(request, 'accounts/login.html', {'form': form})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        auth_logout(request)
        return redirect('films:homepage')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'accounts/profile.html', {'user': user})