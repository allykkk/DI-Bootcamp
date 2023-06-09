from __future__ import absolute_import
from braces.views import AnonymousRequiredMixin, FormValidMessageMixin, LoginRequiredMixin, MessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import CreateView, FormView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .forms import SignupForm, LoginForm, BookingSearchForm
from .models import Room


# index page that shows hotel information
def index(request):
    return render(request, 'index.html')


# visitors sign up
class SignUpView(CreateView, AnonymousRequiredMixin, FormValidMessageMixin):
    form_class = SignupForm
    success_url = reverse_lazy('visitors:login')
    template_name = 'visitors/register.html'
    form_valid_message = "Sign Up Success!"


# visitors log in
class LoginView(FormView, AnonymousRequiredMixin, FormValidMessageMixin):
    form_class = LoginForm
    success_url = reverse_lazy('index')
    template_name = 'visitors/login.html'
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


# visitors log out
class LogOutView(RedirectView, LoginRequiredMixin, MessageMixin):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super(LogOutView, self).get(request, *args, **kwargs)


class BookingSearchView(FormView):
    template_name = 'visitors/search.html'
    form_class = BookingSearchForm
    success_url = reverse_lazy('visitors:result')

    def form_valid(self, form):
        params = {
            'group_size': form.cleaned_data['group_size'],
            'check_in_date': form.cleaned_data['check_in_date'],
            'check_out_date': form.cleaned_data['check_out_date']
        }
        parameters = self.success_url + "?" + urlencode(params)
        return redirect(parameters)

class AvailableRoomView(ListView):
    model = Room
    template_name = 'visitors/search_results.html'

    def get_queryset(self):
        group_size = int(self.request.GET.get("group_size"))
        check_in_date = self.request.GET.get("check_in_date")
        check_out_date = self.request.GET.get("check_out_date")
        object_list = Room.objects.exclude(room_type__capacity__lt=group_size)
        object_list = object_list.exclude(booking__check_in_date__range=(check_in_date, check_out_date))
        object_list = object_list.exclude(booking__check_out_date__range=(check_in_date, check_out_date))

        return object_list.distinct("room_type__room_name")
