from django.contrib import admin
from .models import Theme, Booking


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'time', 'numPeople', 'theme']


admin.site.register(Booking, BookingAdmin)
admin.site.register(Theme, ThemeAdmin)