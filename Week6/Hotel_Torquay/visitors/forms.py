from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.forms import HiddenInput

from .models import Booking


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn-primary')
            )
        )


class BookingSearchForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['group_size', 'check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(
                attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(
                attrs={'type': 'date'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget = HiddenInput()

    def is_valid(self):
        if not super().is_valid(): return False
        # If it actually IS valid, check that it's not in DB
        current_booking = self.save(commit=False)
        similar_bookings_count = Booking.objects.filter(check_in_date=current_booking.check_in_date,
                                                        check_out_date=current_booking.check_out_date,
                                                        room=current_booking.room).count()
        print(f"Found {similar_bookings_count} similar bookings")
        return similar_bookings_count == 0