from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Librarian, Visitors
from .serializers import LibrarianSerializer, VisitorSerializer
from rest_framework.permissions import AllowAny
from datetime import datetime
from django.http import Http404
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class LibrarianViewSet(viewsets.ModelViewSet): 
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]


class MainLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Main')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]

class DumingagLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Dumingag')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]
    
class PagadianLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Pagadian')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]
    
    
class CanutoLibrarians(viewsets.ModelViewSet):
    queryset = Librarian.objects.filter(site='Canuto')
    serializer_class = LibrarianSerializer
    permission_classes = [AllowAny]
    

class VisitorCount(APIView):
    def post(self, request):
        ip_address = request.data.get('ip_address')
        user_agent = request.data.get('user_agent')
        anonymous_uuid = request.data.get('anonymous_uuid')
        today = datetime.now().date()

        # Check if a visitor with the same IP address and date already exists
        visitor_exists = Visitors.objects.filter(ip_address=ip_address, timestamp__date=today).exists()

        if not visitor_exists:
            # Create a new visitor
            visitor = Visitors.objects.create(ip_address=ip_address, user_agent=user_agent, anonymous_uuid=anonymous_uuid)
            visitor.save()
            return Response({'message': 'Visitor recorded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Visitor already recorded today.'}, status=status.HTTP_200_OK)
