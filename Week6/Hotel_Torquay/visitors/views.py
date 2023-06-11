from __future__ import absolute_import
from datetime import datetime
from braces.views import AnonymousRequiredMixin, FormValidMessageMixin, LoginRequiredMixin, MessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import CreateView, FormView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .forms import SignupForm, LoginForm, BookingSearchForm, BookingForm
from .models import Room, Booking


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
    template_name = 'new-ui/search.html'
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
        self.group_size = int(self.request.GET.get("group_size"))
        self.check_in_date = self.request.GET.get("check_in_date")
        self.check_out_date = self.request.GET.get("check_out_date")

        available_rooms_list = Room.get_free_rooms(self.check_in_date, self.check_out_date)
        final_result = Room.filter_capacity(available_rooms_list, self.group_size)

        return final_result.distinct('room_type__capacity', 'room_type__room_name')


class MakeBookingView(FormView):
    form_class = BookingForm
    model = Booking
    template_name = "visitors/booking.html"
    success_url = "index.html"
    rendered = False

    def post(self, *args, **kwargs):
        return render(self.request, 'visitors/booking.html', self.post_page_context())

    def post_page_context(self):
        data = {}

        # Fill context with received data
        data['room_type'] = self.request.POST.get("room_type")
        data['group_size'] = self.request.POST.get("group_size")
        data['check_in_date'] = self.request.POST.get("check_in_date")
        data['check_out_date'] = self.request.POST.get("check_out_date")

        # Fill context with pretty strings for UI
        data['check_in_fmt'] = datetime.strptime(data['check_in_date'], '%Y-%m-%d').strftime('%a, %b %d, %Y')
        data['check_out_fmt'] = datetime.strptime(data['check_out_date'], '%Y-%m-%d').strftime('%a, %b %d, %Y')
        total_length = (datetime.strptime(data['check_out_date'], '%Y-%m-%d') - datetime.strptime(data['check_in_date'],
                                                                                                  '%Y-%m-%d')).days
        data['nights_fmt'] = total_length

        # Find the user's room
        available_rooms_list = Room.get_free_rooms(data['check_in_date'], data['check_out_date'])
        filtered_capacity = Room.filter_capacity(available_rooms_list, data['group_size'])
        final_results = Room.filter_type(filtered_capacity, data['room_type']).first()
        data['price'] = total_length * (final_results.room_type.price_per_night)
        data['selected_room'] = final_results
        data['user'] = self.request.user.id

        return data


class ConfirmedBookingFormView(FormView):
    form_class = BookingForm
    context_object_name = "booking"
    model = Booking
    template_name = "visitors/booking_success.html"

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.save()
            context = {
                'booking_id': data.id
            }
            return render(request, 'visitors/booking_success.html', context)
        return render(request, 'index.html')
