from __future__ import absolute_import
from braces.views import AnonymousRequiredMixin, FormValidMessageMixin, LoginRequiredMixin, MessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .forms import SignupForm, LoginForm, ImageForm, ProfileForm
from .models import Image, Profile


# handle user Sign up
class SignUpView(CreateView, AnonymousRequiredMixin, FormValidMessageMixin):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    form_valid_message = "Sign Up Success!"


# handle user login
class LoginView(FormView, AnonymousRequiredMixin, FormValidMessageMixin):
    form_class = LoginForm
    success_url = reverse_lazy('index')
    template_name = 'registration/login.html'
    form_valid_message = "Log In Success!"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


# handle user log out
class LogOutView(RedirectView, LoginRequiredMixin, MessageMixin):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super(LogOutView, self).get(request, *args, **kwargs)


# show all the uploaded pictures
class ImageListView(ListView):
    model = Image
    template_name = 'image_share/index.html'
    context_object_name = 'images'


class UploadImageView(LoginRequiredMixin, CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'image_share/upload_image.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserImageView(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'image_share/my_images.html'
    context_object_name = 'images'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get_or_create(user=user)[0]
        context['image_count'] = profile.image_count
        return context

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
