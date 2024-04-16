from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Librarian, Visit

class LibrarianSerializer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'
        
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'