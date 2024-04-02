from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Librarian, Visitors

class LibrarianSerializer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'
        
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = ('id', 'ip_address', 'user_agent', 'timestamp', 'anonymous_uuid')