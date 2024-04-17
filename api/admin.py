from django import forms
from django.contrib import admin
from .models import Librarian, Visit, Booking

class CustomTimeInput(forms.TimeInput):
    input_type = 'time'

    def __init__(self, attrs=None, format='%I:%M %p'):
        super().__init__(attrs=attrs, format=format)

class BookingAdminForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'startDatetime': CustomTimeInput(),
            'endDatetime': CustomTimeInput(),
        }

class BookingAdmin(admin.ModelAdmin):
    form = BookingAdminForm
    list_display = ['event', 'month', 'startDatetime', 'endDatetime']

admin.site.register(Booking, BookingAdmin)


admin.site.register(Librarian)
admin.site.register(Visit)
