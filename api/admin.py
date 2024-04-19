from django import forms
from django.contrib import admin
from .models import Librarian, Booking
from django.utils.html import format_html

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


class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_image', 'name', 'position', 'email', 'site', 'is_librarian_head', 'facebook_link')  
    list_filter = ('is_librarian_head', 'site')  

    def display_image(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px; border-radius:50%;" />', obj.user_image.url)
    display_image.short_description = 'Image'

admin.site.register(Librarian, LibrarianAdmin)
