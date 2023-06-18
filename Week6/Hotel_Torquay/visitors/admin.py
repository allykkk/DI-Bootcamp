from django.contrib import admin
from .models import Room,Booking,UserRequest
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','user','room','check_in_date','check_out_date']


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','message']


admin.site.register(Room)

admin.site.register(Booking,BookingAdmin)

admin.site.register(UserRequest,UserRequestAdmin)