from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from phonebook.models import Person


class PhoneNumberFilter(SimpleListFilter):
    title = _('Phone Number')
    parameter_name = 'phone_number'

    def lookups(self, request, model_admin):
        persons = Person.objects.distinct('phone_number').values('phone_number')
        return [(person['phone_number'], person['phone_number']) for person in persons]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(phone_number=self.value())
        return queryset


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'formatted_phone_number', 'address')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = (PhoneNumberFilter,)

    def formatted_phone_number(self, obj):
        return obj.phone_number.as_international

    formatted_phone_number.short_description = 'Phone Number'
    formatted_phone_number.admin_order_field = 'phone_number'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['phone_number'].widget = PhoneNumberInternationalFallbackWidget()
        return form


admin.site.register(Person, PersonAdmin)
