from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, SignupForm
from .models import CustomUser
from django.contrib.auth import login as auth_login

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


    def post(self,request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('homepage')
        return render(request, 'login.html', {'form': form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("gifs:homepage")


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        print("a")
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
        return render(request, 'signup.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        user = request.user
        return render(request, 'profile.html', {'user': user})
