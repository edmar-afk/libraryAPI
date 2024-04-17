from django.contrib import admin
from .models import Librarian, Visit, Booking

admin.site.register(Librarian)
admin.site.register(Visit)
admin.site.register(Booking)