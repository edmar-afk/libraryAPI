from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Librarian, Visit, Booking
from datetime import datetime, time
class LibrarianSerializer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'
        
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    startDatetime = serializers.SerializerMethodField()
    endDatetime = serializers.SerializerMethodField()

    def get_startDatetime(self, obj):
        # Combine month field with startDatetime
        start_datetime = datetime.combine(obj.month, obj.startDatetime)
        return start_datetime.strftime('%Y-%m-%dT%H:%M')

    def get_endDatetime(self, obj):
        # Combine month field with endDatetime
        end_datetime = datetime.combine(obj.month, obj.endDatetime)
        return end_datetime.strftime('%Y-%m-%dT%H:%M')

    class Meta:
        model = Booking
        fields = ['event', 'month', 'startDatetime', 'endDatetime']